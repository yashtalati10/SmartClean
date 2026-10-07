from ..core.profiler import DataProfiler

def generate_profile(dataframe):
    profiler = DataProfiler(dataframe)
    return profiler.profile()