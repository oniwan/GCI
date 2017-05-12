def main():
  def get_ticker(ticker_list):
    for ticker in ticker_list:
      yield ticker
          
  def get_period(period_list):
    for period in period_list:
      yield period[0],period[1]
  
  ticker_list = ["3382","1605","1612"]
  period_list = ((2011,2012),(2012,2013),(2013,2014))
    
  ticker = get_ticker(ticker_list)
  print ticker
    
  period_list = get_period(period_list)
    
  print period
if "__name__" == "__main__":
  main()                    
