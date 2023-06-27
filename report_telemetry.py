import pytlm
from pytlm import LogSession

tlm_opts = {
    'subset': ['Half Skidpad CW [#1] 000', 'Warmup m40 C0 [#1] 003'],
    'resample': True,
    'resample_interval_us': 1000,
    'align': True
}

logs = LogSession('2022_12_12_Vadena', options=tlm_opts)

