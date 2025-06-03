def mood_tracker():

   print("Vítej v denním duševním deníčku ")

   name = input("Zadej své jméno: ")

   try:
       mood_score = int(input("Jak se dnes cítíš (1–10)? "))

       if mood_score < 1 or mood_score > 10:

           print("Zadej číslo mezi 1 a 10.")

           return
   except ValueError: 
       print("Zadej prosím číslo.")

       return

   emotion = input("Jakou emoci dnes nejvíc cítíš (např. veselý, unavený, smutný...)? ")

   day_summary = input("Popiš svůj den jednou větou: ")

   print("\nZpracovávám tvoje odpovědi...\n")

   print(f"Ahoj {name}!")

   print(f"Dnes jsi ohodnotil/a svou náladu jako {mood_score} a cítíš se {emotion}.")

   print(f"Tvé shrnutí dne: \"{day_summary}\"")

   if mood_score <= 4:

       print("Doporučení: Dej si pauzu, odpočiň si a popovídej si s někým blízkým.")

   elif 5 <= mood_score <= 7:

       print("Doporučení: Dopřej si něco příjemného – třeba procházku nebo oblíbený film.")

   else:

       print("Skvělé! Měj radost z hezkého dne a třeba si to zapiš jako vzpomínku!")

   print("Děkujeme, že sis udělal/a čas na sebe. ")