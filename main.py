from zoneinfo import ZoneInfo
import gifos
from math import floor
from random import randint
from datetime import datetime

FPS = 10
FONT_FILE_LOGO = "./fonts/RubikLines.ttf"
FONT_FILE_BITMAP = "./fonts/Perfect DOS VGA 437 Win.ttf"
t = gifos.Terminal(800, 500, 15, 15, FONT_FILE_BITMAP, 15)


def seconds(s):
    return floor(FPS * s)


def command(text, row, count, args=None):
    col = t.curr_col
    t.toggle_show_cursor(True)
    t.gen_typing_text(f"\x1b[91m{text[:-1]}", row, contin=True)
    t.delete_row(row, col)
    t.gen_text(f"\x1b[92m{text}\x1b[0m", row, count=count, contin=True)
    if args:
        t.gen_typing_text(args, row, contin=True)


t.set_fps(FPS)
t.set_prompt("\x1b[31mjlvlg\x1b[0m@\x1b[33mlevelos ~> \x1b[0m")

t.gen_text("", 1, count=seconds(1))
t.toggle_show_cursor()
t.gen_text("Level OS BIOS v2.1", 1)
t.gen_text("Copyright (C) 2024, \x1b[31mLevelling Solutions\x1b[0m", 2)
t.gen_text("MOS Technology 6510/8500 @ 1.023 MHz", 3)
t.gen_text(
    "Press \x1b[94mDEL\x1b[0m to enter SETUP, \x1b[94mESC\x1b[0m to cancel Memory Test",
    t.num_rows,
)
for i in range(0, 65653, randint(5000, 10000)):
    t.delete_row(7)
    if i < 30000:
        t.gen_text(f"Memory Test: {i}", 7, count=2, contin=True)
    else:
        t.gen_text(f"Memory Test: {i}", 7, contin=True)
t.delete_row(7)
t.gen_text("Memory Test: 64KB OK", 7, count=seconds(0.5), contin=True)
t.gen_text("", 11, count=seconds(0.5), contin=True)
t.clear_frame()

t.gen_text("Initiating Boot Sequence", 1, contin=True)
t.gen_typing_text(".....", 1, contin=True)
t.gen_text("\x1b[96m", 1, count=0, contin=True)
t.set_font(FONT_FILE_LOGO, 66)
os_logo_text = "Level OS"
mid_row = (t.num_rows) // 2
mid_col = (t.num_cols - len(os_logo_text) + 1) // 2
effect_lines = gifos.effects.text_scramble_effect_lines(
    os_logo_text, 3, include_special=False
)
for line in effect_lines:
    t.delete_row(mid_row + 1)
    t.gen_text(line, mid_row + 1, mid_col + 1)
t.clear_frame()

t.set_font(FONT_FILE_BITMAP)
t.clone_frame(seconds(1 / 3))
t.gen_text("\x1b[93mLevel OS v2.1 (tty1)\x1b[0m", 1, count=seconds(1 / 3))
t.gen_text("login: ", 3, count=seconds(1 / 3))
t.toggle_show_cursor()
t.gen_typing_text("jlvlg", 3, contin=True)
t.gen_text("", 4, count=seconds(1 / 3))
t.toggle_show_cursor()
t.gen_text("password: ", 4, count=seconds(1 / 3))
t.toggle_show_cursor()
t.gen_typing_text("*********", 4, contin=True)
t.toggle_show_cursor()
time_now = datetime.now(ZoneInfo("America/Recife")).strftime(
    "%a %b %d %I:%M:%S %p %Z %Y"
)
t.gen_text(f"Last login: {time_now} on tty1", 6)

t.gen_prompt(7, count=5)
command("clear", 7, seconds(1 / 5))

git_user_details = gifos.utils.fetch_github_stats("jlvlg")
user_age = gifos.utils.calc_age(1, 2, 2003)
t.clear_frame()
top_languages = [lang[0] for lang in git_user_details.languages_sorted]
user_details_lines = f"""
\x1b[30;101mjlvlg@GitHub\x1b[0m
--------------
\x1b[96mOS:     \x1b[93mArch Linux, Windows 11\x1b[0m
\x1b[96mHost:   \x1b[93mUniversidade Federal do Agreste de Pernambuco \x1b[94m#UFAPE\x1b[0m
\x1b[96mKernel: \x1b[93mCiência da Computaçao \x1b[94m#BCC\x1b[0m
\x1b[96mUptime: \x1b[93m{user_age.years} years, {user_age.months} months, {user_age.days} days\x1b[0m
\x1b[96mIDE:    \x1b[93mVSCode\x1b[0m

\x1b[30;101mContact:\x1b[0m
--------------
\x1b[96mEmail:      \x1b[93mj.lucasvinicius03@gmail.com\x1b[0m
\x1b[96mLinkedIn:   \x1b[93mjose-lucas-vinicius-lopes-gama\x1b[0m

\x1b[30;101mGitHub Stats:\x1b[0m
--------------
\x1b[96mUser Rating: \x1b[93m{git_user_details.user_rank.level}\x1b[0m
\x1b[96mTotal Stars Earned: \x1b[93m{git_user_details.total_stargazers}\x1b[0m
\x1b[96mTotal Commits (2023): \x1b[93m{git_user_details.total_commits_last_year}\x1b[0m
\x1b[96mTotal PRs: \x1b[93m{git_user_details.total_pull_requests_made}\x1b[0m
\x1b[96mMerged PR %: \x1b[93m{git_user_details.pull_requests_merge_percentage}\x1b[0m
\x1b[96mTotal Contributions: \x1b[93m{git_user_details.total_repo_contributions}\x1b[0m
\x1b[96mTop Languages: \x1b[93m{', '.join(top_languages[:5])}\x1b[0m
"""
t.gen_prompt(1)
prompt_col = t.curr_col
t.clone_frame(10)
t.toggle_show_cursor(True)
command("fetch.sh", 1, 1, " -u jlvlg")
t.gen_text(user_details_lines, 2, count=5, contin=True)
t.gen_prompt(t.curr_row + 1)
t.gen_typing_text(
    "\x1b[92m# Have a nice day kind stranger :D Thanks for stopping by!",
    t.curr_row,
    contin=True,
)
t.save_frame("fetch_details.png")
t.gen_text("", t.curr_row, count=80, contin=True)
t.gen_gif()

readme_file_content = rf"""<div align="justify">
<picture>
<img alt="Level OS" src="./output.gif">
</picture>
</div>
<table>
  <tr>
    <td>
      <a href="https://github.com/jlvlg/aedii-projeto"
        ><img
          src="https://github-readme-stats.vercel.app/api/pin/?username=jlvlg&repo=aedii-projeto"
          alt=""
      /></a>
    </td>
    <td>
      <a href="https://github.com/jlvlg/IP-Projeto-C"
        ><img
          src="https://github-readme-stats.vercel.app/api/pin/?username=jlvlg&repo=IP-Projeto-C"
          alt=""
      /></a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/jlvlg/IP-Projeto-Python"
        ><img
          src="https://github-readme-stats.vercel.app/api/pin/?username=jlvlg&repo=IP-Projeto-Python"
          alt=""
      /></a>
    </td>
    <td>
      <a href="https://github.com/jlvlg/Pentagon"
        ><img
          src="https://github-readme-stats.vercel.app/api/pin/?username=jlvlg&repo=Pentagon"
          alt=""
      /></a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/jlvlg/reserva-ai"
        ><img
          src="https://github-readme-stats.vercel.app/api/pin/?username=jlvlg&repo=reserva-ai"
          alt=""
      /></a>
    </td>
    <td>
      <a href="https://github.com/jlvlg/automato-com-pilha"
        ><img
          src="https://github-readme-stats.vercel.app/api/pin/?username=jlvlg&repo=automato-com-pilha"
          alt=""
      /></a>
    </td>
  </tr>
</table>
"""
with open("README.md", "w") as fp:
    fp.write(readme_file_content)
    print("INFO: README.md file generated")
