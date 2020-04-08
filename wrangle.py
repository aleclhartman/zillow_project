import numpy as np
import pandas as pd

import env

def get_db_url(dbname) -> str:
    url = 'mysql+pymysql://{}:{}@{}/{}'
    return url.format(env.user, env.password, env.host, dbname)

zillow_query = """SELECT prop.bathroomcnt, prop.bedroomcnt, prop.calculatedfinishedsquarefeet, prop.fips, plut.propertylandusedesc, prop.taxvaluedollarcnt, prop.taxamount, (prop.taxamount/prop.taxvaluedollarcnt) as tax_rate, pred.transactiondate
FROM properties_2017 as prop
JOIN predictions_2017 as pred USING(parcelid)
JOIN propertylandusetype as plut USING(propertylandusetypeid)
WHERE prop.propertylandusetypeid = 261
AND pred.transactiondate >= "2017-05-01"
AND pred.transactiondate <= "2017-06-30"
ORDER BY pred.transactiondate;
"""

url = get_db_url("zillow")

def wrangle_zillow():
    df = pd.read_sql(zillow_query, url)
    df["fips"] = df["fips"].astype("int")
    df["county"] = df["fips"].map({6037: "Los Angeles County", 6059: "Orange County", 6111: "Ventura County"})
    df.rename(columns={"bathroomcnt": "bathrooms", "bedroomcnt": "bedrooms", "calculatedfinishedsquarefeet": "square_feet", "fips": "fips_code", "propertylandusedesc": "property_description", "taxvaluedollarcnt": "tax_value", "taxamount": "tax_amount", "transactiondate": "transaction_date"}, inplace=True)
    df = df.dropna()
    df.reset_index(inplace=True)
    df.drop(columns="index", inplace=True)
    return df