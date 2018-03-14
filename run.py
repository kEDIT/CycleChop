

class Schema:
    def __init__(self,df=None,df_type=None):
        if df is None:
            raise InvalidCsvException
        else:
            try:
                import pandas as pd
                df = pd.read_csv()
            except Exception as e:
                pass

