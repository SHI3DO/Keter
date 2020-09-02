import shutil
import os
import asyncio

loop = asyncio.get_event_loop()


async def build_dpdocs():
    return await loop.run_in_executor(None, _build_dpdocs)


def _build_dpdocs():
    shutil.rmtree("discord.py-master/docs/locale")
    shutil.copytree("loc/locale", "discord.py-master/docs/locale")

    owd = os.getcwd()
    os.chdir("./discord.py-master/docs")
    os.system("convert_html.bat")
    os.chdir(owd)

    shutil.copytree("discord.py-master/docs/_build/html", "temp")
    for file_list in os.listdir("docsweb"):
        if file_list not in [".git", "CNAME", "README.md", "_static", "style.css", ".nojekyll"]:
            try:
                os.remove(f"docsweb/{file_list}")
                shutil.copy(f"temp/{file_list}", f"docsweb/{file_list}")
            except PermissionError:
                shutil.rmtree(f"docsweb/{file_list}")
                shutil.copytree(f"temp/{file_list}", f"docsweb/{file_list}")
    shutil.rmtree("temp")
