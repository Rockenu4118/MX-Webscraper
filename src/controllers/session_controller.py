import time
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
from scraper.response_fetcher import fetch_response
from scraper.response_logger import log_response
from scraper.response_parser import parse_response
from utils.util import time_elapsed
from config.config import pg_base_url


class SessionController:        
    def run_session(self, progress_bar):
        start_time = time.perf_counter()

        ids = self.generate_ids(range(self.starting_id, self.ending_id))
        responses = []
        parsed_responses = []

        with progress_bar as progress:
            get_responses = progress.add_task("[red] Getting responses...", total=self.total_ids)

            with ThreadPoolExecutor(max_workers=self.workers) as pool:
                futures = [pool.submit(fetch_response, *(self.base_url, id)) for id in ids]
                for future in futures:
                    result = future.result()
                    responses.append(result)
                    progress.update(get_responses, advance=1)

            parse_responses = progress.add_task("[blue] Parsing responses...", total=self.total_ids)

            for response in responses:
                parsed_response = parse_response(*response)
                parsed_responses.append(parsed_response)
                progress.update(parse_responses, advance=1)

            log_responses = progress.add_task("[green] Logging responses...", total=self.total_ids)

            for response in parsed_responses:
                try:
                    log_response(*response)
                except Exception as e:
                    pass
                finally:
                    progress.update(log_responses, advance=1)

        end_time = time.perf_counter()

        return time_elapsed(start_time, end_time)
    
    def configure_session(self, base_url=pg_base_url, starting_id=1, ending_id=10, workers=1):
        self.base_url    = base_url
        self.starting_id = starting_id
        self.ending_id   = ending_id
        self.total_ids   = ending_id - starting_id
        self.workers     = workers

    def generate_ids(self, range):
        ids = []
        for id in range:
            ids.append(id)
        return ids
    
    
    