transparent = "rgba(0,0,0,0)"
brand_blue_100 = "rgba(51, 102, 204, 1)"
tab_font_grey = "rgba(173, 216, 230, 0.3)"

height = "auto"

container_style = {
    "height": height,
    "width": "100%",
    "margin": 0,
    "padding-right": 0,
    "padding-left": 0,
}

body_style = {
    "background-image": 'url("/assets/images/body.png")',
    "background-repeat": "no-repeat",
    "background-size": "cover",
    "height": height,
    "border": "1px white solid",
    "width": "100%",
    "margin": 0,
    "padding": 0,
}

""" __________________________________________________________________ """
"""                                NAVBAR                              """
""" __________________________________________________________________ """

navbar_background_style = {
    "background-image": 'url("/assets/images/navbar.png")',
    "background-size": "cover",
    "height": height,
    "textAlign": "center",
    "font-family": "Impact, white, sans-serif",
    "margin": 0,
    "border": "1px white solid",
    "width": "100%",
}

""" __________________________________________________________________ """
"""                         NAVBAR - LOGO                              """
""" __________________________________________________________________ """

navbar_logo_style = {
    "margin-top": 20,
    "height": "auto",
    "display": "block",
    "margin-left": "auto",
    "margin-right": "auto",
    "width": "90%",
}

navbar_logo_subtitle_style = {
    "width": "100%",
    "height": "auto",
    "margin-top": 0,
    "margin-bottom": 0,
    "text-shadow": "2px 2px 0 #4074b5, 2px -2px 0 #4074b5, -2px 2px 0 #4074b5, -2px -2px 0 #4074b5, 2px 0px 0 #4074b5, 0px 2px 0 #4074b5, -2px 0px 0 #4074b5, 0px -2px 0 #4074b5, 2px 2px 2px rgba(173,255,110,0), 2px 2px 2px rgba(173,255,110,0)",
    "color": "ivory",
    "font-size": "100%",
}


""" __________________________________________________________________ """
"""                         NAVBAR - ACTIVE USER                       """
""" __________________________________________________________________ """

active_user_card_style = {
    "background": transparent,
    "padding-left": "5%",
    "padding-right": "5%",
    "margin-left": 5,
    "margin-right": 5,
    "border": "1px lightblue solid",
}

active_user_card_body_style = {
    "margin": 0,
    "background": transparent,
    "border-bottom": "1px lightblue solid",
    "font-family": "Oswald, sans-serif",
    "height": "auto",
    "width": "100%",
}

active_user_card_footer_icons = {
    "background": transparent,
    "color": "lightblue",
    "font-size": 24,
    "margin-top": "8%",
}

active_user_box = {
    "margin-top": 0,
    "margin-bottom": 20,
    "margin-left": "3%",
    "margin-right": "3%",
}
""" __________________________________________________________________ """
"""                            NAVBAR - TABS                           """
""" __________________________________________________________________ """

tab_component_styles = {
    "padding": "5%",
    "width": "100%",
    "margin-top": -5,
    "margin-bottom": -5,
}

tab_style = {
    "background": transparent,
    "padding": "8px",
    "color": tab_font_grey,
    "font-family": "Oswald, sans-serif",
    "width": "100%",
}

tab_selected_style = {
    "background": transparent,
    "text-shadow": "0px 0px 7px rgba(13, 10, 205, 0.75)",
    "font-family": "Oswald, sans-serif",
    "color": "white",
    "padding": "8px",
    "width": "100%",
    "border-top": "3px solid lightblue",
}

""" __________________________________________________________________ """
"""                               CONTENT                              """
""" __________________________________________________________________ """

# background_style = {
#     "background-image": 'url("/assets/images/body.png")',
#     "background-repeat": "no-repeat",
#     "background-size": "cover",
#     "margin": 0,
#     "padding": 0,
#     "height": 752,
#     "width": "100%",
# }

header_box_style = {
    "-webkit-box-shadow": "-2px 9px 17px -3px rgba(0,0,0,0.75)",
    "-moz-box-shadow": "-2px 9px 17px -3px rgba(0,0,0,0.75)",
    "box-shadow": "-2px 9px 17px -3px rgba(0,0,0,0.75)",
    "background": transparent,
    "font-family": "Oswald Light, sans-serif",
    "font-size": 26,
    "color": "white",
    "margin-top": 8,
    "margin-left": 5,
    "height": 56,
    "border-top": "10px rgba(173, 216, 230, 0.3) solid",
    "border-left": "1px rgba(173, 216, 230, 0.3) solid",
    "border-right": "1px rgba(173, 216, 230, 0.3) solid",
    "border-bottom": "1px rgba(173, 216, 230, 0.2) solid",
    "padding": 3,
    "textAlign": "center",
}

graph_box_title_style = {
    "font-family": "Oswald ExtraLight, sans-serif",
    "font-size": 18,
    "color": "white",
    "margin": 0,
    "height": 35,
}

key_facts_logo_style = {"margin-top": 280, "margin-left": 40, "height": 100}

key_facts_title_style = {
    "font-family": "Oswald Light, sans-serif",
    "font-size": 70,
    "color": "white",
    "text-align": "center",
    "margin-top": 0,
    "margin-left": "auto",
    "margin-right": "auto",
    "height": 100,
}

key_facts_subtitle_style = {
    "font-family": "Oswald ExtraLight, sans-serif",
    "font-size": 30,
    "text-align": "center",
    "margin-top": 0,
    "color": "rgba(153, 153, 204, 1)",
    "margin-left": "auto",
    "margin-right": "auto",
    "height": 100,
}

key_facts_boxes_style = {
    "margin-top": -40,
    "height": 100,
    "width": 120,
    "display": "block",
    "margin-left": "50%",
    "margin-right": "50%",
    "border-top": "1px rgba(102, 102, 153, 0.75) solid",
    "border-bottom": "1px rgba(102, 102, 153, 0.75) solid",
}

key_facts_period_style = {
    "font-family": "Oswald ExtraLight, sans-serif",
    "font-size": 20,
    "text-align": "center",
    "margin-top": 10,
    "color": "white",
    "margin-left": "auto",
    "margin-right": "auto",
    "height": 100,
}
