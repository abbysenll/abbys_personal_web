from nicegui import ui

'''
    STEPS TO UPDATE
        make update
        TERMINAL COMMANDS IN ORDER
        
git add .
git commit -m "changed"
git push

'''



# WEBSITE INSPIRATION :
        # https://braydenfriesen.com
        # https://chester.how

# PLANNING
    # COLOUR SCHEME :
        # navy : #0E1627
        # mauve : #7F6269
        # peach : #BD8E89
        # light peach : #E5C5C1
        # very light peach : #F4E1E0

    # FONTS :
        # 'IM Fell French Canon', serif; (secondary text)
        # 'IM Fell Double Pica', serif; (headers/titles)
        # 'Cormorant', serif; (body texts)

# FAVICON
ui.add_head_html("""
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='0.9em' font-size='90'%3E✿%3C/text%3E%3C/svg%3E">
""", shared=True)

# GOOGLE FONT LOADER
ui.add_head_html("""
<link href="https://fonts.googleapis.com/css2?family=IM+Fell+French+Canon:ital@0;1&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=IM+Fell+Double+Pica:ital@0;1&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Cormorant:ital,wght@0,300..700;1,300..700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/simple-icons-font@v13/font/simple-icons.min.css">
""", shared=True)

# STYLE DEFINER
NAV_STYLE = """
color: #7F6269;
text-decoration: none;
font-family: 'IM Fell French Canon', serif;
font-size: 20px;
font-weight: bold;
"""

TITLE_STYLE = """
        color: #7F6269;
        font-family: "IM Fell Double Pica", serif;
        font-size: 50px;
        width: 100%;
        text-align: center;
        font-weight: 400;
        margin-top: 60px;
        """

def navbar():
    with ui.header().style("""
        margin: 12px 20px;
        padding: 18px 24px;

        background: #E5C5C1;

        border-radius: 7px;

        backdrop-filter: blur(4px);
        -webkit-backdrop-filter: blur(4px);

        box-shadow:
            0 10px 30px rgba(127, 98, 105, 0.18),
            0 0 20px rgba(229, 197, 193, 0.15),
            inset 0 1px 0 rgba(255, 255, 255, 0.2),
            inset 0 -1px 0 rgba(127, 98, 105, 0.03);

        width: calc(100% - 40px);
    """).classes('items-center justify-between shadow-md px-6'):
        ui.label("Abigayle Snelson").classes("text-2xl").style(NAV_STYLE)

        with ui.row().classes("gap-6"):
            ui.link("Home", "#home").style(NAV_STYLE)
            ui.link("About Me", "#about").style(NAV_STYLE)
            ui.link("Projects", "#projects").style(NAV_STYLE)
            ui.link("Skills", "#skills").style(NAV_STYLE)
            ui.link("Contact", "#contact").style(NAV_STYLE)


@ui.page("/")
def home():
    navbar()
    ui.add_head_html('''

        <style>
        html {
        scroll-behavior: smooth;
        }
        
        body {
            background-color: #F4E1E0;
        }
        .nicegui-content {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        </style>
        ''')

    with ui.column().props('id=home').classes("items-center"):
        with ui.column().style("""
        color: #7F6269;
        font-family: "IM Fell Double Pica", serif;
        font-size: 50px;
        width: 700px;
        max-width: 100%;
        text-align: center;
        font-weight: 400;
        margin-top: 60px;
        background: #E5C5C1;
        backdrop-filter: blur(4px);
        -webkit-backdrop-filter: blur(4px);
        margin: 12px 20px;
        padding: 18px 24px;
        border-radius: 10px;
        items-align: center;
        border: 2px solid rgba(127, 98, 105, 0.48);
        box-shadow:
            0 10px 30px rgba(127, 98, 105, 0.18),
            0 0 20px rgba(229, 197, 193, 0.15),
            inset 0 1px 0 rgba(255, 255, 255, 0.2),
            inset 0 -1px 0 rgba(127, 98, 105, 0.03);
        """):
            ui.label("Hello, my name is").style("""
            color: #7F6269;
            font-family: "IM Fell Double Pica", serif;
            font-size: 40px;
            width: 100%;
            max-width: 100%;
            text-align: center;
            font-weight: 400;
            margin-top: 20px;
            """)
            ui.label("Abigayle Snelson").style("""
        color: #7F6269;
        font-family: "IM Fell Double Pica", serif;
        font-size: 50px;
        width: 100%;
        max-width: 100%;
        text-align: center;
        font-weight: 600;
        margin-top: 10px;
        background: rgba(244, 225, 224, 0.38);
        backdrop-filter: blur(4px);
        -webkit-backdrop-filter: blur(4px);
        padding: 18px 24px;
        border-radius: 10px;
        box-shadow:
            0 10px 30px rgba(127, 98, 105, 0.18),
            0 0 20px rgba(229, 197, 193, 0.15),
            inset 0 1px 0 rgba(255, 255, 255, 0.2),
            inset 0 -1px 0 rgba(127, 98, 105, 0.03);
        """)

    with ui.column().props('id=about'):
        ui.label("About Me").style(TITLE_STYLE)

    with ui.column().props('id=projects'):
        ui.label("Projects").style(TITLE_STYLE)

    with ui.column().props('id=skills'):
        ui.label("Skills").style(TITLE_STYLE)
        with ui.row().classes("gap-8; items-center;"):
            with ui.card().style("background-color: rgba(127, 98, 105, 0.78); border-radius: 8px; width: 150px; "
                                 "border: 3px solid rgba(127, 98, 105)").classes("items-center"):
                ui.html('<i class="si si-python" style="font-size:60px; color:#F4E1E0;"></i>')
                ui.label("Python").style("""
                                   color:#F4E1E0;
                                   font-family:'Cormorant', serif;
                                   font-size:30px;
                                   font-weight: 700;
                               """)

            with ui.card().style("background-color: rgba(127, 98, 105, 0.78); border-radius: 8px; width: 150px; "
                                 "border: 3px solid rgba(127, 98, 105)").classes("items-center"):
                ui.html('<i class="si si-python" style="font-size:60px; color:#F4E1E0;"></i>')
                ui.label("Python").style("""
                                   color:#F4E1E0;
                                   font-family:'Cormorant', serif;
                                   font-size:30px;
                                   font-weight: 700;
                               """)

            with ui.card().style("background-color: rgba(127, 98, 105, 0.78); border-radius: 8px; width: 150px; "
                                 "border: 3px solid rgba(127, 98, 105)").classes("items-center"):
                ui.html('<i class="si si-python" style="font-size:60px; color:#F4E1E0;"></i>')
                ui.label("Python").style("""
                                   color:#F4E1E0;
                                   font-family:'Cormorant', serif;
                                   font-size:30px;
                                   font-weight: 700;
                               """)

    with ui.column().props('id=contact'):
        ui.label("Contact").style(TITLE_STYLE)


ui.run(
    title="Abigayle S Personal Website",
    host="0.0.0.0",
    port=8080,
    favicon="✿"
)