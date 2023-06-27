import time
import csv
from concurrent.futures import ThreadPoolExecutor
from scraper.response_fetcher import fetch_response
from scraper.response_logger import log_response
from scraper.response_parser import parse_response
from utils.util import time_elapsed
from config.config import pg_base_url


class SessionController:        
    def run_session(self, progress_bar):
        start = time.perf_counter()

        ids = self.generate_ids(range(self.starting_id, self.ending_id))


        with progress_bar as progress:
            player_progress = progress.add_task("[red] Scraping...", total=self.total_ids)

            with ThreadPoolExecutor(max_workers=self.workers) as pool:
                futures = [pool.submit(fetch_response, *(self.base_url, id)) for id in ids]
                for future in futures:
                    response = future.result()
                    progress.update(player_progress, advance=1)
                    parsed_response = parse_response(*response)

                    try:
                        log_response(*parsed_response)
                    except Exception as e:
                        pass

        end = time.perf_counter()

        return time_elapsed(start, end)
    
    def configure_session(self, base_url=pg_base_url, starting_id=1, ending_id=10, workers=1):
        self.base_url    = base_url
        self.starting_id = starting_id
        self.ending_id   = ending_id
        self.total_ids   = ending_id - starting_id
        self.workers     = workers

    def format_logs(self):
        with open('./logs/players.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                "Id",
                "name",
                "grad_year",
                "position",
                "height",
                "weight",
                "bat",
                "throw",
                "state",
                "rating"
            ])

        with open('./logs/metric_sets.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                "player_id",
                "exit_velo",
                "of_velo",
                "if_velo",
                "sixty",
                "fb_velo"
            ])

    def generate_ids(self, range):
        ids = []
        for id in range:
            ids.append(id)
        return ids
    
    
    