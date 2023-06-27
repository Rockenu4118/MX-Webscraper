from bs4 import BeautifulSoup
from models.page_attributes import PageAttributes

def parse_response(id, response):
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
        pop        = page.find(id="ContentTopLevel_ContentPlaceHolder1_lblPGEventResultsCPop")
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
            pop,
            fb_velo
        )

        return id, page_attributes