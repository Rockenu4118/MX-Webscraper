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
from page_attributes import PageAttributes
from logger import Logger
from util import Util

class Scraper:

    def __init__(self):
        self.progress_bar = Progress(
            TextColumn("[progress.description]{task.description}"),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            BarColumn(),
            MofNCompleteColumn(),
            TimeElapsedColumn(),
            TextColumn("•"),
            TimeRemainingColumn(),
            TextColumn("•"),
            TextColumn("[progress.speed]{task.speed} iter/s"),
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
    
    def parse_response(self, id, response):
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

        page_attributes = PageAttributes(
            name,
            grad_year,
            position,
            height,
            weight,
            handedness,
            state,
            rating,
            exit_velo,
            of_velo,
            if_velo,
            sixty,
            fb_velo
        )

        return id, page_attributes
    
    def log_response(self, id, page_attributes):

        name       = page_attributes.name.text
        grad_year  = page_attributes.grad_year.text[:4]            if page_attributes.grad_year  != None else 0
        position   = page_attributes.position.text                 if page_attributes.position   != None else "n/a"
        height     = Converter.height(page_attributes.height.text) if page_attributes.height     != None else 0
        weight     = page_attributes.weight.text.strip()           if page_attributes.weight     != None else 0
        bat_hand   = page_attributes.handedness.text.split("/")[0] if page_attributes.handedness != None else "n/a"
        throw_hand = page_attributes.handedness.text.split("/")[1] if page_attributes.handedness != None else "n/a"
        state      = page_attributes.state.text[-2:]               if page_attributes.state      != None else "n/a"
        rating     = page_attributes.rating.text                   if page_attributes.rating     != None else 0

        exit_velo = page_attributes.exit_velo.text if page_attributes.exit_velo != None else 0
        of_velo   = page_attributes.of_velo.text   if page_attributes.of_velo   != None else 0
        if_velo   = page_attributes.if_velo.text   if page_attributes.if_velo   != None else 0
        sixty     = page_attributes.sixty.text     if page_attributes.sixty     != None else 0
        fb_velo   = page_attributes.fb_velo.text   if page_attributes.fb_velo   != None else 0

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

        return
    
    def configure_session(self, base_url, starting_id, ending_id, workers):
        self.base_url    = base_url
        self.starting_id = starting_id
        self.ending_id   = ending_id
        self.total_ids   = ending_id - starting_id
        self.workers     = workers

    def run_session(self):
        start_time = time.perf_counter()

        ids = self.generate_ids(range(self.starting_id, self.ending_id))
        responses = []
        parsed_responses = []

        with self.progress_bar as progress:
            get_responses = progress.add_task("[red] Getting responses...", total=self.total_ids)

            with ThreadPoolExecutor(max_workers=self.workers) as pool:
                futures = [pool.submit(self.get_response, id) for id in ids]
                for future in futures:
                    result = future.result()
                    responses.append(result)
                    progress.update(get_responses, advance=1)

            parse_responses = progress.add_task("[blue] Parsing responses...", total=self.total_ids)

            for response in responses:
                parsed_response = self.parse_response(*response)
                parsed_responses.append(parsed_response)
                progress.update(parse_responses, advance=1)

            log_responses = progress.add_task("[green] Logging responses...", total=self.total_ids)

            for response in parsed_responses:
                try:
                    self.log_response(*response)
                except Exception as e:
                    pass
                finally:
                    progress.update(log_responses, advance=1)

        end_time = time.perf_counter()

        return Util.time_elapsed(start_time, end_time)


