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

    # *** BRAINSTORMING COLOUR SCHEME : ***
        # navy -> cafe noir : 4C3D19
        # mauve -> kombu green : 354024
        # peach -> moss green : 889063
        # light peach -> tan : CFBB99
        # very light peach -> bone/cream white : E5D7C4

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

# GLOBAL STYLE RESET
ui.add_head_html("""
<style>
* {
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

html, body {
    margin: 0;
    padding: 0;
    width: 100%;
}

body {
    background-color: #F4E1E0;
}

.nicegui-content {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
}
</style>
""", shared=True)

# STYLE DEFINER
NAV_STYLE = """
color: #CFBB99;
text-decoration: none;
font-family: 'IM Fell French Canon', serif;
font-size: 20px;
font-weight: bold;
"""

TITLE_STYLE = """
        color: #4C3D19;
        font-family: "IM Fell Double Pica", serif;
        font-size: 40px;
        width: 100%;
        text-align: center;
        font-weight: 400;
        margin-top: 60px;
        """

def navbar():
    with ui.header().style("""
        margin: 12px 20px;
        padding: 18px 24px;

        background: #354024;
        border: 2px solid #CFBB99;
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
            background-color: #889063;
        }
        .nicegui-content {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        </style>
        ''')

# HOME CATEGORY
    with ui.column().props('id=home').classes("items-center"):
        ui.label("About Me").style(f"""{TITLE_STYLE}; font-size: 10px; margin-top: 20px; color: rgba(127, 98, 105, 
        0);""")
        # NAMECARD
        with ui.column().style("""
        color: #7F6269;
        font-family: "IM Fell Double Pica", serif;
        font-size: 50px;
        width: min(700px, 90vw);
        max-width: 100%;
        text-align: center;
        font-weight: 400;
        margin-top: 60px;
        background: #CFBB99;
        backdrop-filter: blur(4px);
        -webkit-backdrop-filter: blur(4px);
        margin: 12px 20px;
        padding: 18px 24px;
        border-radius: 10px;
        items-align: center;
        border: 2px solid #4C3D19;
        box-shadow:
            0 10px 30px rgba(127, 98, 105, 0.18),
            0 0 20px rgba(229, 197, 193, 0.15),
            inset 0 1px 0 rgba(255, 255, 255, 0.2),
            inset 0 -1px 0 rgba(127, 98, 105, 0.03);
        """):
            # INNER TEXT
            ui.label("Hello, my name is").style("""
            color: #4C3D19;
            font-family: "IM Fell Double Pica", serif;
            font-size: 30px;
            width: 100%;
            max-width: 100%;
            text-align: center;
            font-weight: 400;
            margin-top: 20px;
            """)
            ui.label("Abigayle Snelson").style("""
        color: #4C3D19;
        font-family: "IM Fell Double Pica", serif;
        font-size: clamp(32px, 5vw, 40px);
        width: 100%;
        max-width: 100%;
        text-align: center;
        font-weight: 600;
        margin-top: 10px;
        background: rgba(229, 215, 196, 0.38);
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

# ABOUT ME CATEGORY
    with ui.column().props('id=about'):
        ui.label("About Me").style(TITLE_STYLE)

# PROJECTS CATEGORY
    with ui.column().props('id=projects'):
        ui.label("Projects").style(TITLE_STYLE)

    # PROJECT 1
    with ui.row().classes("w-full"):
        with ui.grid(columns=2).classes("w-full").style("""
        color: #7F6269;
        font-family: "IM Fell Double Pica", serif;
        font-size: 50px;
        width: min(1100px, 90vw);
        max-width: 100%;
        text-align: center;
        font-weight: 400;
        margin-top: 60px;
        background: #4C3D19;
        backdrop-filter: blur(4px);
        -webkit-backdrop-filter: blur(4px);
        margin: 12px 20px;
        padding: 18px 24px;
        border-radius: 10px;
        items-align: center;
        border: 2px solid rgba(53, 64, 36, 0.48);
        box-shadow:
            0 10px 30px rgba(127, 98, 105, 0.18),
            0 0 20px rgba(229, 197, 193, 0.15),
            inset 0 1px 0 rgba(255, 255, 255, 0.2),
            inset 0 -1px 0 rgba(127, 98, 105, 0.03);
        """):
            ui.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnxZnbZvsXk53T1xlTyr0akcZc7UqplTdw3LQVYKMRzO4SsF9_uRmwgpY&s=10').style("""
                    font-family: "IM Fell Double Pica", serif;
                    font-size: clamp(32px, 5vw, 40px);
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
            with ui.card().style("""
        color: #7F6269;
        font-family: "IM Fell Double Pica", serif;
        font-size: clamp(32px, 5vw, 40px);
        width: 100%;
        max-width: 100%;
        text-align: center;
        font-weight: 600;
        margin-top: 10px;
        background: rgba(53, 64, 36);
        backdrop-filter: blur(4px);
        -webkit-backdrop-filter: blur(4px);
        padding: 18px 24px;
        border-radius: 10px;
        box-shadow:
            0 10px 30px rgba(127, 98, 105, 0.18),
            0 0 20px rgba(229, 197, 193, 0.15),
            inset 0 1px 0 rgba(255, 255, 255, 0.2),
            inset 0 -1px 0 rgba(127, 98, 105, 0.03);
        """):
                ui.label("Title").style(f"""{TITLE_STYLE}; color: #CFBB99;""")
                ui.label("Description").style(f"""{NAV_STYLE}; text-align: center; width: 100%;""")

    # PROJECT 2
    with ui.row().classes("w-full"):
        ui.space()
        with ui.grid(columns=2).classes("w-full").style("""
        color: #7F6269;
        font-family: "IM Fell Double Pica", serif;
        font-size: 50px;
        width: min(1100px, 90vw);
        max-width: 100%;
        text-align: center;
        font-weight: 400;
        margin-top: 60px;
        background: #4C3D19;
        backdrop-filter: blur(4px);
        -webkit-backdrop-filter: blur(4px);
        margin: 12px 20px;
        padding: 18px 24px;
        border-radius: 10px;
        items-align: center;
        border: 2px solid rgba(53, 64, 36, 0.48);
        box-shadow:
            0 10px 30px rgba(127, 98, 105, 0.18),
            0 0 20px rgba(229, 197, 193, 0.15),
            inset 0 1px 0 rgba(255, 255, 255, 0.2),
            inset 0 -1px 0 rgba(127, 98, 105, 0.03);
        """):
            ui.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnxZnbZvsXk53T1xlTyr0akcZc7UqplTdw3LQVYKMRzO4SsF9_uRmwgpY&s=10').style("""
                    font-family: "IM Fell Double Pica", serif;
                    font-size: clamp(32px, 5vw, 40px);
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
            with ui.card().style("""
        color: #7F6269;
        font-family: "IM Fell Double Pica", serif;
        font-size: clamp(32px, 5vw, 40px);
        width: 100%;
        max-width: 100%;
        text-align: center;
        font-weight: 600;
        margin-top: 10px;
        background: rgba(53, 64, 36);
        backdrop-filter: blur(4px);
        -webkit-backdrop-filter: blur(4px);
        padding: 18px 24px;
        border-radius: 10px;
        box-shadow:
            0 10px 30px rgba(127, 98, 105, 0.18),
            0 0 20px rgba(229, 197, 193, 0.15),
            inset 0 1px 0 rgba(255, 255, 255, 0.2),
            inset 0 -1px 0 rgba(127, 98, 105, 0.03);
        """):
                ui.label("Title").style(f"""{TITLE_STYLE}; color: #CFBB99;""")
                ui.label("Description").style(f"""{NAV_STYLE}; text-align: center; width: 100%;""")

    # PROJECT 3
    with ui.row().classes("w-full"):
        with ui.grid(columns=2).classes("w-full").style("""
        color: #7F6269;
        font-family: "IM Fell Double Pica", serif;
        font-size: 50px;
        width: min(1100px, 90vw);
        max-width: 100%;
        text-align: center;
        font-weight: 400;
        margin-top: 60px;
        background: #4C3D19;
        backdrop-filter: blur(4px);
        -webkit-backdrop-filter: blur(4px);
        margin: 12px 20px;
        padding: 18px 24px;
        border-radius: 10px;
        items-align: center;
        border: 2px solid rgba(53, 64, 36, 0.48);
        box-shadow:
            0 10px 30px rgba(127, 98, 105, 0.18),
            0 0 20px rgba(229, 197, 193, 0.15),
            inset 0 1px 0 rgba(255, 255, 255, 0.2),
            inset 0 -1px 0 rgba(127, 98, 105, 0.03);
        """):
            ui.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnxZnbZvsXk53T1xlTyr0akcZc7UqplTdw3LQVYKMRzO4SsF9_uRmwgpY&s=10').style("""
                    font-family: "IM Fell Double Pica", serif;
                    font-size: clamp(32px, 5vw, 40px);
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
            with ui.card().style("""
        color: #7F6269;
        font-family: "IM Fell Double Pica", serif;
        font-size: clamp(32px, 5vw, 40px);
        width: 100%;
        max-width: 100%;
        text-align: center;
        font-weight: 600;
        margin-top: 10px;
        background: rgba(53, 64, 36);
        backdrop-filter: blur(4px);
        -webkit-backdrop-filter: blur(4px);
        padding: 18px 24px;
        border-radius: 10px;
        box-shadow:
            0 10px 30px rgba(127, 98, 105, 0.18),
            0 0 20px rgba(229, 197, 193, 0.15),
            inset 0 1px 0 rgba(255, 255, 255, 0.2),
            inset 0 -1px 0 rgba(127, 98, 105, 0.03);
        """):
                ui.label("Title").style(f"""{TITLE_STYLE}; color: #CFBB99;""")
                ui.label("Description").style(f"""{NAV_STYLE}; text-align: center; width: 100%;""")

# SKILLS CATEGORY
    with ui.column().props('id=skills'):
        ui.label("Skills").style(TITLE_STYLE)
        with ui.row().classes("gap-8; items-center;"):
            # CARD 1
            with ui.card().style("background-color: #4C3D19; border-radius: 8px; width: 150px; "
                                 "border: 3px solid #E5D7C4").classes("items-center"):
                ui.html('<i class="si si-python" style="font-size:60px; color:#E5D7C4;"></i>')
                ui.label("Python").style("""
                                   color:#E5D7C4;
                                   font-family:'Cormorant', serif;
                                   font-size:30px;
                                   font-weight: 700;
                               """)
                ui.tooltip("Primary language; ~1 year building web apps and personal projects.").classes(
                    'text-lg rounded-xl '
                    'shadow-md').style("""
                    background-color: #4C3D19;
                    font-family: 'Cormorant', serif;
                    font-style: bold;
                    """)

            # CARD 2
            with ui.card().style("background-color: #4C3D19; border-radius: 8px; width: 150px; "
                                 "border: 3px solid #E5D7C4").classes("items-center"):
                ui.html('<i class="si si-python" style="font-size:60px; color:#E5D7C4;"></i>')
                ui.label("Python").style("""
                                   color:#E5D7C4;
                                   font-family:'Cormorant', serif;
                                   font-size:30px;
                                   font-weight: 700;
                               """)

            # CARD 3
            with ui.card().style("background-color: #4C3D19; border-radius: 8px; width: 150px; "
                                 "border: 3px solid #E5D7C4").classes("items-center"):
                ui.html('<i class="si si-python" style="font-size:60px; color:#E5D7C4;"></i>')
                ui.label("Python").style("""
                                   color:#E5D7C4;
                                   font-family:'Cormorant', serif;
                                   font-size:30px;
                                   font-weight: 700;
                               """)

# CONTACT ME CATEGORY
    with ui.column().props('id=contact').classes("gap-4"):
        ui.label("Contact Me").style(TITLE_STYLE)
        with ui.column().style("""
            width: 100%;
            background: #E5D7C4;

            border: 2px solid #4C3D19;
            border-radius: 10px;

            padding: 15px 15px 15px 15px;
            margin-top: 20px;
            
            box-shadow:
                0 -10px 30px rgba(127, 98, 105, 0.18),
                inset 0 1px 0 rgba(255, 255, 255, 0.2);
        """):
            with ui.row().classes("w-full gap-20 items-center"):

                # LINK HOLDER
                with ui.row().classes("items-center justify-center gap-6"):

                    # GITHUB
                    with ui.row().classes("items-center gap-2"):
                        ui.html('<i class="si si-github" style="color: #4C3D19;"</i>')
                        ui.link("GitHub", "https://github.com/abbysenll", new_tab=True).style(f"""{NAV_STYLE}; 
                        color: #4C3D19""")

                    ui.label("|").style(f"""{NAV_STYLE}; 
                        color: #4C3D19""")

                    # LINKEDIN
                    with ui.row().classes("items-center gap-2"):
                        ui.html('<i class="si si-linkedin" style="color: #4C3D19;"</i>')
                        ui.link("LinkedIn",
                                "https://www.linkedin.com/in/abigayle-snelson-8b4b55395/?skipRedirect=true",
                                new_tab=True
                                ).style(f"""{NAV_STYLE}; 
                        color: #4C3D19""")

                    ui.label("|").style(f"""{NAV_STYLE}; 
                        color: #4C3D19""")

                    # GMAIL
                    with ui.row().classes("items-center gap-2"):
                        ui.html('<i class="si si-gmail" style="color: #4C3D19;"</i>')
                        ui.label("snelsonabby@gmail.com").style(f"""{NAV_STYLE}; 
                        color: #4C3D19""")


ui.run(
    title="Abigayle S Personal Website",
    host="0.0.0.0",
    port=8080,
    favicon="✿"
)