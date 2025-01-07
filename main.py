from pathlib import Path

from app.interpolate_fr import interpolate_from_file
from app.plot import plot, generate_color
from app.normalize_fr import normalize
from app.hrtf import compensate
from app.tilt import tilt_phone
from config import HPTF_NORMALIZATION_FREQUENCY

# Setup
headphone_name = "hd600_fresh_pads"  # Change here !
# Available headphones currently:
# sundara (Hifiman)
# hd600_fresh_pads (Sennheiser)
# hd800s (Sennheiser)
# hd560s (Sennheiser)
# m50x (Audio-technica)

display_name = headphone_name.capitalize()
lowered_name = headphone_name.lower()

# Baselines
gras = Path("baselines/kb50xx_dfhrtf_baseline.txt")
bk_5128 = Path("baselines/b&k_5128_dfhrtf_baseline.txt")
baseline_gras = normalize(interpolate_from_file(gras))
baseline_5128 = normalize(interpolate_from_file(bk_5128))

# Phones (headphone frequency responses)
phone_gras = normalize(
    interpolate_from_file(
        Path(f"frequency_responses/kb50xx/{lowered_name}_gras.txt"),
    )
)
phone_5128 = normalize(
    interpolate_from_file(
        Path(
            f"frequency_responses/b&k_5128/{lowered_name}_5128.txt")
    )
)

# Remove HRTF effects, keep HpTF effects only
hptf_gras = normalize(
    compensate(baseline_gras, phone_gras),
    freq=HPTF_NORMALIZATION_FREQUENCY
)
hptf_5128 = normalize(
    compensate(baseline_5128, phone_5128),
    freq=HPTF_NORMALIZATION_FREQUENCY
)

# Calculate the variation of HpTF
delta = compensate(
    hptf_5128,
    hptf_gras
)
# Divide it by 2 (to center the graph later)
divided_delta_db = delta[1]/2

plot(
    phone_names=[f"{display_name} HpTF effect on GRAS",
                 f"{display_name} HpTF effect on B&K 5128"],
    phone_list=[hptf_gras, hptf_5128],
    show_area=False
)
plot(
    phone_name=f"Delta of HPtf of {display_name}",
    phone_list=[(delta[0], divided_delta_db),
                (delta[0], -divided_delta_db)],
    show_area=True,
    color=generate_color()
)
plot(
    phone_name=f"{display_name} compensated frequency response on GRAS relative to -1dB/oct DF",
    phone_list=[normalize(compensate(tilt_phone(baseline_gras), phone_gras))],
    show_area=True,
    add_x_axis_line=True
)
plot(
    phone_name=f"{display_name} compensated frequency response on B&K 5128 relative to -1dB/oct DF",
    phone_list=[normalize(compensate(tilt_phone(baseline_5128), phone_5128))],
    show_area=True,
    add_x_axis_line=True

)
