import re

def normalize(text: str) -> str:
    text = re.sub(r'`([^`]+)`', r'\1', text)
    text = re.sub(r'[\u2018\u2019\u0060\u00B4]', "'", text)
    text = re.sub(r'[\u201C\u201D]', '"', text)
    text = re.sub(r'[\u2013\u2014\u2012\u2015]', '-', text)
    text = re.sub(r'^\s*\[.*?\]\s*', '', text)
    text = re.sub(r'!?\[([^\]]*)\]\([^\)]+\)', r'\1', text)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'(\*\*|__|\*|_)', '', text)
    text = re.sub(r'(?m)^[#>]\s*', '', text)
    return re.sub(r'\s+', ' ', text.lower().strip())

def chunk_matches(expected: str, retrieved: str, minimum: int = 60) -> bool:
    expected, retrieved = normalize(expected), normalize(retrieved)
    if not expected or not retrieved:
        return False
    prefix = expected[: min(150, len(expected))]
    if len(prefix) >= minimum and prefix in retrieved:
        return True
    maximum = min(len(expected), len(retrieved), 150)
    for size in range(maximum, minimum - 1, -1):
        for start in range(maximum - size + 1):
            if expected[start : start + size] in retrieved:
                return True
    return False

expected = 'ly the surface rainfall but also the three-dimensional structure of latent heat release in the tropics. While the primary structure information from TRMM was to come from its first-ever spaceborne rain radar, there was a great desire to expand the profiling work to the TRMM Microwave Imager (TMI) in order to gain both from its much wider swath and pave the way to utilizing available sensors such a'
retrieved = '''[The Evolution of the Goddard Profiling Algorithm to a Fully Parametric Scheme > 1. Introduction]\nstructure information from TRMM was to come from its first-ever spaceborne rain radar, there was a great desire to expand the profiling work to the TRMM Microwave Imager (TMI) in order to gain both from its much wider swath and pave the way to utilizing available sensors such as the Special Sensor Microwave Imager (SSM/I) (Hollinger et al. 1990), which had been available since 1987. The algorithm was thus designed from its very inception to be *parametric* in the sense that the algorithm would work with any passive microwave sensor as long as the sensor characteristics and channel errors were properly specified. While it has taken a number of iterations, this paper describes GPROF 2014, the fully parametric algorithm, as well as the recent versions of the algorithm leading to it. The current impetus is provided by the Global Precipitation Measurement (GPM) (Hou et al. 2014), which explicitly seeks to provide  \nCorresponding author address: Christian D. Kummerow, Department of Atmospheric Science, Colorado State University, 200 West Lake Street, 1371 Campus Delivery, Fort Collins, CO 80523-1371.  \nE-mail: kummerow@atmos.colostate.edu  \nDOI: 10.1175/JTECH-D-15-0039.1'''

print(chunk_matches(expected, retrieved))
