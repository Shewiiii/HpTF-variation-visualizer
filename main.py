from pathlib import Path
from app.interpolate_fr import interpolate_from_file
from app.plot import plot_frequency_response
from app.normalize_fr import normalize

gras = Path("baselines/gras_dfhrtf_baseline.txt")
hd600_gras = Path("frequency_responses/gras/hd600_fresh_pads_gras.txt")

baseline = interpolate_from_file(gras)
headphone = interpolate_from_file(hd600_gras)
normalized_baseline = normalize(baseline, reference_freq=1000)
normalized_headphone = normalize(headphone, reference_freq=1000)

print(plot_frequency_response([normalized_baseline, normalized_headphone]))