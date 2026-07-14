from openai import openai # Installa il pacchetto openai

openai.api_key = "API key" # Inserisci la API key.
if not openai.api.key: # Check per vedere se è valida
    print("API key non valida.")
    exit(0) # Se fallisce il check esce con cod. 1 (Err)  
if openai.api.key: # Check passato
    print("API key valida.") # Se la API key è valida procede con lo script

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Scrivi un testo breve"}])
if  not completion.choices: # Prompt non valido 
    print("Errore: Un errore si è verificato. Controlla la tua API key o il prompt inserito.")
else: exec(completion.choices[0].message.content) # Funziona solo con prompt valido.
print("Prompt valido.") 
exit(1) # Esce con cod 1 (successo)  