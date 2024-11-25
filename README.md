# Object-Detection

Suite à de nombreux problèmes, je n'ai réussi à faire marcher Mask_RCNN que via TensorFlow 2.0.

Fichiers de log:

10 Epochs :

![Captureia10](https://github.com/user-attachments/assets/facea24e-9b39-4390-b59e-e0c8bdd95516)

20 Epochs :

![Captureia20](https://github.com/user-attachments/assets/0a9a6068-b691-4c58-90a2-24c63b19bb63)

30 Epochs avec une image de validation non labelisée :

![Captureiabis](https://github.com/user-attachments/assets/884250e7-11f9-4865-8f50-d11fa3286de2)

Analyse : 

Dans les trois cas, nous sommes en situation d'overfitting. L'utilisation de 20 epochs est plus adaptée car c'est le cas avec le loss le plus bas sans pour autant qu'il y ait une trop grande différence avec le val_loss. On peut le voir avec les résultats ci-dessous.

Résultats (Epochs 10, 20 puis 30) : 

![Capture11](https://github.com/user-attachments/assets/552a80a9-8747-4d30-bc20-c14ebf8b6d3b)
![Captureia11](https://github.com/user-attachments/assets/090a8765-7a0c-40fb-b9fb-2e6587f55c49)
![Capture11](https://github.com/user-attachments/assets/07c60074-23e0-4a11-9e3e-da62d550f58d)

![Capture10](https://github.com/user-attachments/assets/415326dc-9562-4ca1-a435-5e868c3fedd3)
![Captureia10](https://github.com/user-attachments/assets/20c3dd5e-6655-42fd-a083-dbfce1c2ba96)
![Capture10](https://github.com/user-attachments/assets/bdbd497b-9db2-4d73-bbb8-c2eef2fef928)

![Capture8](https://github.com/user-attachments/assets/98c08497-b9a0-46af-9fa3-0a1be992ac23)
![Captureia8](https://github.com/user-attachments/assets/0f475bcf-8e17-4a4b-9c60-fa5299117be0)
![Capture8](https://github.com/user-attachments/assets/3f63cbe5-c6a0-4fa6-9443-5b94a6cb7f39)


![Capture7](https://github.com/user-attachments/assets/df16b1c0-04eb-4512-88c5-688a05487fcd)
![Captureia7](https://github.com/user-attachments/assets/b27f726e-1851-4d3b-8b27-b2b7be98b25f)
![Capture7](https://github.com/user-attachments/assets/8a997f83-20f0-4996-963b-eba6b07c7019)


![Capture6](https://github.com/user-attachments/assets/b6c50ea5-ca73-4b24-979c-98f973ca53a7)
![Captureia6](https://github.com/user-attachments/assets/ac2c5cc9-3fb2-490d-90a8-c72e9d08ea70)
![Capture6](https://github.com/user-attachments/assets/13878e0f-7a85-4631-8c94-e0078651cffb)


![Capture4](https://github.com/user-attachments/assets/6cdaab03-db11-4780-ad46-01de5c062002)
![Captureia4](https://github.com/user-attachments/assets/13df48f5-26e0-4e11-9e80-0f5ae60b57c4)
![Capture4](https://github.com/user-attachments/assets/05862882-4c35-4425-ba52-512bbdf5a45d)


![Capture3](https://github.com/user-attachments/assets/d7e71e87-3755-454f-90c9-604106a0b526)
![Captureia3](https://github.com/user-attachments/assets/681906fb-01f5-4661-be4a-b1017330c20c)
![Capture3](https://github.com/user-attachments/assets/7f5edf28-ca1a-4bae-bd38-c0db6ef832ce)


![Capture1](https://github.com/user-attachments/assets/ff843a35-62a5-4801-b8a7-5d83b83e9486)
![Captureia1](https://github.com/user-attachments/assets/9d35ac84-e37b-43aa-a250-da2614e60383)
![Capture1](https://github.com/user-attachments/assets/bab769da-77d7-4f95-9e85-e0ecfa44e754)

Les résultats sont globalement bons mais il y a des problèmes.
Les problèmes sont variés : 

Non détection de baguettes dans l'image, détection partielle de la baguette, détection parfaite d'une baguette mais partielle pour les autres dans l'image, détection d'une baguette sur une image de croissant, fusion de baguettes, détection de plusieurs baguettes dans une seule

Je soupçonne ma labelisation d'en être la cause principale.

5 Epochs avec optimizer Adam, learning rate 0.001 : 

![image](https://github.com/user-attachments/assets/89124ee8-71b5-4587-b281-7ebcb42ecf24)

Ici, nous avons des erreurs. On va alors tester avec une autre valeur de learning rate

5 Epochs avec optimizer Adam, learning rate 0.0001 :

![image](https://github.com/user-attachments/assets/798f21ec-7511-4ec3-999d-9bc7aeabe427)

Ici, nous sommes dans un cas d'underfitting, qui peut être causé par le nombre d'epochs trop bas. Il faudrait tester avec plus d'epochs.

