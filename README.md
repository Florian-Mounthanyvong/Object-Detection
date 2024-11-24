# Object-Detection

Fichiers de log:

10 Epochs :

![Captureia10](https://github.com/user-attachments/assets/facea24e-9b39-4390-b59e-e0c8bdd95516)

20 Epochs :

![Captureia20](https://github.com/user-attachments/assets/0a9a6068-b691-4c58-90a2-24c63b19bb63)

30 Epochs avec une image de validation non labelisée :

![Captureiabis](https://github.com/user-attachments/assets/884250e7-11f9-4865-8f50-d11fa3286de2)

Analyse : 

Des trois cas ci-dessus, l'utilisation de 20 epochs est plus adaptée car c'est le cas avec le loss le plus bas sans pour autant qu'il y ait une grande différence avec le val_loss. On peut le voir avec les résultats ci-dessous.

Résultats : 

![Capture1](https://github.com/user-attachments/assets/8964b843-c077-4047-b7f2-c8ec7ec1f6e4)
![Capture12](https://github.com/user-attachments/assets/cd63b098-171e-4db0-907d-a710dba57f46)
![Capture11](https://github.com/user-attachments/assets/e79ed04c-3599-4fee-a1d1-6269ef5c5211)
![Capture10](https://github.com/user-attachments/assets/12d16609-2a2c-4ede-a47c-b908a6e4bf02)
![Capture9](https://github.com/user-attachments/assets/15b41270-606f-47c5-a222-743277161db1)
![Capture8](https://github.com/user-attachments/assets/99da8755-6510-48e0-b291-52b47d3b9d81)
![Capture7](https://github.com/user-attachments/assets/4dc4bed4-0bf8-4361-8865-f6233d044724)
![Capture5](https://github.com/user-attachments/assets/109d9342-3629-41ed-a0ea-ecf9633c946c)
![Capture4](https://github.com/user-attachments/assets/7dc09b0c-66fe-4641-a810-6616c6bc7612)
EPOCH 20
![Captureia17](https://github.com/user-attachments/assets/bf2eb9b8-cff9-4a5f-81cd-30e63cda2af7)
![Captureia16](https://github.com/user-attachments/assets/f55d2e45-b54a-401b-949c-69f5de4f0a93)
![Captureia15](https://github.com/user-attachments/assets/187817a3-e6ee-4e64-a75a-7a2880acc284)
![Captureia14](https://github.com/user-attachments/assets/05ff4825-2183-4d5d-9c02-4b5b0356316f)
![Captureia13](https://github.com/user-attachments/assets/60cce9a0-faf6-4cfa-b5f0-0399a2c78cd7)
![Captureia11](https://github.com/user-attachments/assets/734df540-28e1-485a-a229-99486da38d6f)
![Captureia6](https://github.com/user-attachments/assets/10d56baf-9e21-4061-b51f-1b69fed03fdb)
![Captureia5](https://github.com/user-attachments/assets/63a05145-a58a-4045-8c1a-bbc8265846ef)
![Captureia4](https://github.com/user-attachments/assets/c2f6a990-483d-4820-8dfd-7e9f1de1c983)
EPOCH 30
![Capture12](https://github.com/user-attachments/assets/c9cc98a6-f189-43a2-be7e-4df2cd863598)
![Capture11](https://github.com/user-attachments/assets/c1857e8e-8e5f-401c-8d36-2618f3505610)
![Capture10](https://github.com/user-attachments/assets/b0107663-c294-4361-a7ba-69a7b61aa340)
![Capture9](https://github.com/user-attachments/assets/09c4bf6a-bfdd-415a-a07a-0800621f0d27)
![Capture8](https://github.com/user-attachments/assets/f6bb052f-127e-46e4-860f-7f4d9dcf6888)
![Capture7](https://github.com/user-attachments/assets/94ae447d-bacc-45fa-8ec4-eef4ec20aeb4)
![Capture5](https://github.com/user-attachments/assets/b4467bc7-66bc-4871-9bbd-8ba9582f3b6b)
![Capture4](https://github.com/user-attachments/assets/d613be25-0667-4ba3-9063-c38f009624a8)
![Capture3](https://github.com/user-attachments/assets/c52d108a-28b1-46b0-b5d9-bcc979ed5d2a)


Les résultats sont globalement bons mais il y a des problèmes.
Les problèmes sont variés : 

Non détection de baguettes dans l'image, détection partielle de la baguette, détection parfaite d'une baguette mais partielle pour les autres dans l'image, détection d'une baguette sur une image de croissant, fusion de baguettes, détection de plusieurs baguettes dans une seule

Je soupçonne ma labelisation d'en être la cause principale.
