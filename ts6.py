from pathlib import Path
import dateparser
import warnings

# Ignore dateparser warnings regarding pytz
warnings.filterwarnings(
    "ignore",
    message="The localize method is no longer necessary, as this time zone supports the fold attribute",
)

def timecr(lines,lines2,la):
    lines.sort()
    lines2.sort()
    la.sort()
    lines = [i[3:] for i in lines]
    lines2 =[i[3:] for i in lines2]
    c = list(zip(lines,lines2))
    tc = [str(abs(dateparser.parse(i[0])-dateparser.parse(i[1]))) for i in c]
    return build_time(tc,la)

def build_time(tc,la):
    final = dict(zip(la,tc))
    sorted_tuple = dict(sorted(final.items(), key=lambda x: x[1]))
    return sorted_tuple

def starter(input):
    filename = "start.log"
    lines = Path(input,filename).read_text().splitlines()
    filename = "end.log"
    lines2 = Path(input,filename).read_text().splitlines()
    filename = "abbreviations.txt"
    la = Path(input,filename).read_text().splitlines()
    return timecr(lines,lines2,la)

starter("dan")