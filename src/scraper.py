import requests
import time
from rich.progress import (
    Progress,
    BarColumn,
    MofNCompleteColumn,
    TextColumn,
    TimeElapsedColumn,
    TimeRemainingColumn
)
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from converter import Converter
from player import Player
from metric_set import MetricSet
from logger import Logger
from util import Util

class Scraper:

    def __init__(self):
        self.progress_bar = Progress(
            TextColumn("[progress.description]{task.description}"),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            BarColumn(),
            MofNCompleteColumn(),
            TextColumn("[progress.speed]{task.speed} iter/s"),
            TextColumn("•"),
            TimeElapsedColumn(),
            TextColumn("•"),
            TimeRemainingColumn()
        )

    def generate_ids(self, range):
        ids = []
        for id in range:
            ids.append(id)
        return ids
    
    def get_response(self, id):
        url = f"{self.base_url}{id}"
        response = requests.get(url)
        return id, response
    
    def handle_response(self, id, response):
        # start = time.perf_counter()
        page = BeautifulSoup(response.text, "lxml")

        name = page.find(id="ContentTopLevel_ContentPlaceHolder1_lblPlayerName")
        if name is None: return

        grad_year  = page.find(id="ContentTopLevel_ContentPlaceHolder1_lblHSGrad")
        position   = page.find(id="ContentTopLevel_ContentPlaceHolder1_lblPos")
        height     = page.find(id="ContentTopLevel_ContentPlaceHolder1_lblHt") 
        weight     = page.find(id="ContentTopLevel_ContentPlaceHolder1_lblWt")
        handedness = page.find(id="ContentTopLevel_ContentPlaceHolder1_lblBT")
        state      = page.find(id="ContentTopLevel_ContentPlaceHolder1_lblHomeTown")
        rating     = page.find(id="ContentTopLevel_ContentPlaceHolder1_lblBestPGGrade")
        exit_velo  = page.find(id="ContentTopLevel_ContentPlaceHolder1_lblPGEventResultsExitVelo")
        of_velo    = page.find(id="ContentTopLevel_ContentPlaceHolder1_lblPGEventResultsOF")
        if_velo    = page.find(id="ContentTopLevel_ContentPlaceHolder1_lblPGEventResultsIF")
        sixty      = page.find(id="ContentTopLevel_ContentPlaceHolder1_lblPGEventResults60")
        fb_velo    = page.find(id="ContentTopLevel_ContentPlaceHolder1_lblPGEventResultsFB")

        name       = name.text
        grad_year  = grad_year.text[:4]            if grad_year  != None else 0
        position   = position.text                 if position   != None else "n/a"
        height     = Converter.height(height.text) if height     != None else 0
        weight     = weight.text.strip()           if weight     != None else 0
        bat_hand   = handedness.text.split("/")[0] if handedness != None else "n/a"
        throw_hand = handedness.text.split("/")[1] if handedness != None else "n/a"
        state      = state.text[-2:]               if state      != None else "n/a"
        rating     = rating.text                   if rating     != None else 0

        exit_velo = exit_velo.text if exit_velo != None else 0
        of_velo   = of_velo.text   if of_velo   != None else 0
        if_velo   = if_velo.text   if if_velo   != None else 0
        sixty     = sixty.text     if sixty     != None else 0
        fb_velo   = fb_velo.text   if fb_velo   != None else 0

        player = Player(
            id,
            name,
            grad_year,
            position,
            height,
            weight,
            bat_hand,
            throw_hand,
            state,
            rating
        )

        metric_set = MetricSet(
            id,
            exit_velo,
            of_velo,
            if_velo,
            sixty,
            fb_velo
        )

        Logger.log_player(player)
        Logger.log_metric_set(metric_set)
        
        # end = time.perf_counter()

        # print(Util.time_elapsed_ms(start, end))

        return
    
    def log_response(self):
        pass
    
    def configure_session(self, base_url, starting_id, ending_id, workers):
        self.base_url = base_url
        self.starting_id = starting_id
        self.ending_id = ending_id
        self.total_ids = ending_id - starting_id
        self.workers = workers

    def run_session(self):
        start_time = time.perf_counter()

        ids = self.generate_ids(range(self.starting_id, self.ending_id))
        responses = []

        with self.progress_bar as progress:
            get_responses = progress.add_task("[red] Getting responses...", total=self.total_ids)

            with ThreadPoolExecutor(max_workers=self.workers) as pool:
                futures = [pool.submit(self.get_response, id) for id in ids]
                for future in futures:
                    result = future.result()
                    responses.append(result)
                    progress.update(get_responses, advance=1)

            handle_responses = progress.add_task("[blue] Handling responses...", total=self.total_ids)

            # with ThreadPoolExecutor(max_workers=self.workers) as pool:
            #     futures = [pool.submit(self.handle_response, *response) for response in responses]
            #     for future in futures:
            #         result = future.result()
            #         progress.update(handle_responses, advance=1)

            for response in responses:
                self.handle_response(*response)
                progress.update(handle_responses, advance=1)

        end_time = time.perf_counter()

        return Util.time_elapsed(start_time, end_time)


