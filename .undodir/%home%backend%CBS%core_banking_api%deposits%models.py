Vim�UnDo� �Υ/��nS^ �Q�R��ew &����L�^[�                                     e)\    _�                     
       ����                                                                                                                                                                                                                                                                                                                                                             ei�    �   
                �   
          5��    
                      K                     �    
                     O                     �    
                 
   O             
       �    
                     X                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ei�    �   
                narration�             5��    
                  G   K             G       5�_�                       F    ����                                                                                                                                                                                                                                                                                                                                                             e)�    �                   �             5��                          �                     �                         �                     �                         �                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e)�     �                   depo�             5��                      B   �             B       5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             e)�    �                5��                       	   D               	       �                         L                      5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e)�     �               import u�             5��                         D                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e)�     �               import uuid5��                         O                      5�_�      	                 B    ����                                                                                                                                                                                                                                                                                                                                                             e)�    �                   deposit_ty �               B    deposit_id = models.UUIDField(default=uuid.uuid4, unique=True)5��       B                 �                     �                         �                     �                     
   �             
       �                        �                    �                         �                     5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                             e)�    �                       �                   deposit_ty�             5��                          �                     �                         �              3       �                                               5�_�   	              
           ����                                                                                                                                                                                                                                                                                                                                                             e)�    �                5��                       	                 	       �               	                 	               5�_�   
                         ����                                                                                                                                                                                                                                                                                                                                                             e)�     �                �             5��                                               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e)�   	 �               	         �                       max_length=255,5��                                      	       �                         '                     �               	                 	               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             e)�     �                �             5��                                               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e)�   
 �               	         �                       blank=True,5��                        2              	       �                         ;                     �               	           3      	               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             e)     �                �             5��                          3                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e)    �               	         �                       null=True,5��                        E              	       �                         N                     �               	           F      	               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             e)     �                �             5��                       G   F              G       5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e)
     �               G        choices=[("deposit", "deposit"), ("withdrawal", "withdrawal")],5��                        Y                    5�_�                       #    ����                                                                                                                                                                                                                                                                                                                                                             e)    �               E        choices=[("check", "deposit"), ("withdrawal", "withdrawal")],5��                        b                    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e)     �               ?        choices=[("check", " "), ("withdrawal", "withdrawal")],�             5��                      !   F             !       5�_�                       1    ����                                                                                                                                                                                                                                                                                                                                                             e)     �               C        choices=[("check", "check"), ("withdrawal", "withdrawal")],5��       '       
          m      
              5�_�                       9    ����                                                                                                                                                                                                                                                                                                                                                             e)    �               =        choices=[("check", "check"), ("cash", "withdrawal")],5��       /       
          u      
              5�_�                       /    ����                                                                                                                                                                                                                                                                                                                                                             e)     �               4        choices=[("check", "check"), ("cash", " ")],�             5��       /                  u                     �               3       7   F      3       7       5�_�                       A    ����                                                                                                                                                                                                                                                                                                                                                             e)    �                   �             5��                          �                     �                         �                     �                        �                    �                         �                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e)    �                   reference_number�             5��                      N   �             N       5�_�                        M    ����                                                                                                                                                                                                                                                                                                                                                             e)[    �                N    reference_number = models.CharField(max_length=255, blank=True, null=True)5��                          �      O               5��