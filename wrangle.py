import numpy as np
import pandas as pd

import env

zillow_query = """SELECT prop.bathroomcnt, prop.bedroomcnt, prop.calculatedfinishedsquarefeet, prop.fips, plut.propertylandusedesc, prop.taxvaluedollarcnt, prop.taxamount, (prop.taxamount/prop.taxvaluedollarcnt) as tax_rate, pred.transactiondate
FROM properties_2017 as prop
JOIN predictions_2017 as pred USING(parcelid)
JOIN propertylandusetype as plut USING(propertylandusetypeid)
WHERE prop.propertylandusetypeid = 261
AND pred.transactiondate >= "2017-05-01"
AND pred.transactiondate <= "2017-06-30"
ORDER BY pred.transactiondate;
"""

url = env.get_db_url("zillow")

def wrangle_zillow():
    df = pd.read_sql(zillow_query, url)
    california_fips = pd.read_csv("california_fips.csv")
    california_fips.drop(columns="Unnamed: 0", inplace=True)
    df = pd.merge(df, california_fips, left_on="fips", right_on="06000", how="left")
    df.drop(columns="06000", inplace=True)
    df.rename(columns={"bathroomcnt": "bathrooms", "bedroomcnt": "bedrooms", "calculatedfinishedsquarefeet": "square_feet", "fips": "fips_code", "propertylandusedesc": "property_description", "taxvaluedollarcnt": "tax_value", "taxamount": "tax_amount", "transactiondate": "transaction_date", "California": "county"}, inplace=True)
    df = df.dropna()
    return df