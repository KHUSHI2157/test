def weekday(num):
    match num:
      case 1:
         print("monday")
      case 2:
        print("tuesday")
      case 3|4:
        print("wednesday or thursday")
      case _:
        print("other day")

        
weekday(3)
    