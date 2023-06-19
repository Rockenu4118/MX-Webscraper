from utils.util import convert_height
from models.player import Player
from models.metric_set import MetricSet

def log_response(id, page_attributes):

        name       = page_attributes.name.text
        grad_year  = page_attributes.grad_year.text[:4]            if page_attributes.grad_year  != None else 0
        position   = page_attributes.position.text                 if page_attributes.position   != None else "n/a"
        height     = convert_height(page_attributes.height.text)   if page_attributes.height     != None else 0
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

        player.log()
        metric_set.log()