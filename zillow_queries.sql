USE zillow;

SELECT prop.id, prop.parcelid, prop.bathroomcnt, prop.bedroomcnt, prop.calculatedfinishedsquarefeet, prop.fips, prop.propertylandusetypeid, plut.propertylandusedesc, prop.unitcnt, prop.taxvaluedollarcnt, prop.taxamount, (prop.taxamount/prop.taxvaluedollarcnt) as tax_rate, pred.transactiondate
FROM properties_2017 as prop
JOIN predictions_2017 as pred USING(parcelid)
JOIN propertylandusetype as plut USING(propertylandusetypeid)
WHERE prop.propertylandusetypeid = 261
AND pred.transactiondate >= "2017-05-01"
AND pred.transactiondate <= "2017-06-30"
ORDER BY pred.transactiondate;

SELECT prop.id, prop.parcelid, prop.bathroomcnt, prop.bedroomcnt, prop.calculatedfinishedsquarefeet, prop.fips, prop.propertylandusetypeid, plut.propertylandusedesc, prop.unitcnt, prop.taxvaluedollarcnt, prop.taxamount, pred.transactiondate
FROM properties_2017 as prop
JOIN predictions_2017 as pred USING(parcelid)
JOIN propertylandusetype as plut USING(propertylandusetypeid)
WHERE prop.propertylandusetypeid = 261
OR prop.unitcnt = 1
ORDER BY pred.transactiondate;