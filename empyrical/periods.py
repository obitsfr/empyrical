APPROX_BDAYS_PER_MONTH = 21
APPROX_BDAYS_PER_YEAR = 252
APPROX_BDAYS_PER_YEAR_BTC = 365

MONTHS_PER_YEAR = 12
WEEKS_PER_YEAR = 52
QTRS_PER_YEAR = 4

DAILY = 'daily'
DAILY_BTC = 'daily BTC'
WEEKLY = 'weekly'
MONTHLY = 'monthly'
QUARTERLY = 'quarterly'
YEARLY = 'yearly'

ANNUALIZATION_FACTORS = {
    DAILY: APPROX_BDAYS_PER_YEAR,
    WEEKLY: WEEKS_PER_YEAR,
    MONTHLY: MONTHS_PER_YEAR,
    QUARTERLY: QTRS_PER_YEAR,
    YEARLY: 1,
    DAILY_BTC: APPROX_BDAYS_PER_YEAR_BTC
}
