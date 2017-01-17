taxesDictionary = {"DE" : 20,
  "UK" : 21,
  "FR" : 20,
  "IT" : 25,
  "ES" : 19,
  "PL" : 21,
  "RO" : 20,
  "NL" : 20,
  "BE" : 24,
  "EL" : 20,
  "CZ" : 19,
  "PT" : 23,
  "HU" : 27,
  "SE" : 23,
  "AT" : 22,
  "BG" : 21,
  "DK" : 21,
  "FI" : 17,
  "SK" : 10,
  "IE" : 21,
  "HR" : 23,
  "LT" : 23,
  "SI" : 24,
  "LV" : 20,
  "EE" : 22,
  "CY" : 21,
  "LU" : 25,
  "MT" : 20}

def getTotal(total, countryCode):
  tax = taxesDictionary[countryCode]
  if total > 2000 and countryCode == "SK":
    tax = 20
  if total <= 11000 and countryCode == "UK":
    return total
  return total + total * (tax / 100)

