Vim�UnDo� w�K������x�ܾ�aM�j�z)��,Uk�Mt   -   $    # Models for all branch managers      $      3       3   3   3    e{�   % _�                             ����                                                                                                                                                                                                                                                                                                                                                             enB    �                # Create your models here.5��                          F                      5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             enD     �                  �               5��                          F                      �                          F                      �                          F                      5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             enF     �                  5��                          F                      5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             enF    �                  5��                          G                      �                          H                      �                        N                     �                        W                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             en\    �                 class Managers(M )�               5��                         X                      �                      %   H              %       5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             en}    �                �             5��                          F               J       5�_�                       %    ����                                                                                                                                                                                                                                                                                                                                                             en�    �                 %class Managers(ManagersCommonFields):5��       %                  �                      �                          �                      �                        �                     �                        �                     5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                             en�     �               5��                          �                      �                          �                      5�_�      
           	           ����                                                                                                                                                                                                                                                                                                                                                             en�     �                  5��                          �                      5�_�   	              
   	        ����                                                                                                                                                                                                                                                                                                                                                             en�     �                  5��                          �                      5�_�   
                 
        ����                                                                                                                                                                                                                                                                                                                                                             en�     �   	               5��    	                      �                      5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             en�     �   
               5��    
                      �                      5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             en�     �                  5��                          �                      5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             en�     �                  5��                          �                      5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             en�     �                  5��                          �                      5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             en�    �                  �               �                  5��                          �                      �                          �               �      5�_�                       #    ����                                                                                                                                                                                                                                                                                                                                                             en�    �         (      %class Managers(ManagersCommonFields):5��       #                  �                      5�_�                       #    ����                                                                                                                                                                                                                                                                                                                                                             en�    �         (      &class Managers(ManagersCommonFields ):�         (    5��       #                  �                      �               %       I   �       %       I       5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             en�   	 �         (          pass5��                        �                     �                        �                     �                        �                     �                          �                      5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             en�   
 �         (           # Models for all branch mana�         (    5��                       $   �               $       5�_�                       $    ����                                                                                                                                                                                                                                                                                                                                                             eo    �      	   )          email  �      	   (      $    # Models for all branch managers5��       $                                       �                                              �       	                  
                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             eo	     �      	   )      	    email�      	   )    5��               	       *         	       *       5�_�                       *    ����                                                                                                                                                                                                                                                                                                                                                             eo    �      
   *      
    roles �      
   )      *    email = models.EmailField(unique=True)5��       *                 +                     �                         0                     �       	                  5                     5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                                             eo    �      
   *      	    roles�   	   
   *    5��               	       +   ,      	       +       �       *                  V                     5�_�                    	   )    ����                                                                                                                                                                                                                                                                                                                                                             eo    �      
   *      *    roles = models.ManyToManyField("Role",�   	   
   *    5��               *       6   ,      *       6       5�_�                    	   5    ����                                                                                                                                                                                                                                                                                                                                                             eo    �      
   *      6    roles = models.ManyToManyField("Role", blank=True)5��       5                  a                     5�_�                    	   8    ����                                                                                                                                                                                                                                                                                                                                                             eo!    �      
   *      :    roles = models.ManyToManyField("Role", blank=True, r )�   	   
   *    5��       8                  d                     �               9       O   ,      9       O       5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ep    �         *       5��                          �                      �                        �                     �                        �                     �                        �                     5�_�                    	   &    ����                                                                                                                                                                                                                                                                                                                                                             ep"     �   	      *    5��    	                      �                     5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                                             ep%    �   
      ,          ob �   	      +          5��    	                      �                     �    	                     �                     �    
                     �                     �    
                     �                     5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ep(     �   
      ,          ob�         ,    5��    
                  !   �             !       5�_�      !                  !    ����                                                                                                                                                                                                                                                                                                                                                             ep)     �   
      ,      !    objects = CustomUserManager()5��    
   !                 �                     5�_�       "           !          ����                                                                                                                                                                                                                                                                                                                                                             ep)    �         .          �         -          5��                          �                     �                         �                     �                          �                     5�_�   !   #           "           ����                                                                                                                                                                                                                                                                                                                                                             ep2    �         .       5��                          �                     �                         �                     5�_�   "   $           #          ����                                                                                                                                                                                                                                                                                                                                                             ep6     �         .          U�         .    5��                         �                    5�_�   #   %           $          ����                                                                                                                                                                                                                                                                                                                                                             ep7    �         .          USERNAME_FIELD = "email"5��                        �                     �                         �                     �                        �                    5�_�   $   &           %          ����                                                                                                                                                                                                                                                                                                                                                             ep=     �         /          REQUIRED_FIELDS = []    5��                         �                     5�_�   %   '           &          ����                                                                                                                                                                                                                                                                                                                                                             ep=    �         .          REQUIRED_FIELDS = []    5��                         �                     5�_�   &   (           '           ����                                                                                                                                                                                                                                                                                                                                                             epA    �         )           �         *           �         +           �         ,           �         -           �         -       5��                                               �                                                �                          �                     �                          �                     �                          �                     5�_�   '   )           (           ����                                                                                                                                                                                                                                                                                                                                                             epG    �         (    5��                          �                      5�_�   (   *           )   )        ����                                                                                                                                                                                                                                                                                                                                                             epO    �   '                      return self.name    �   (               5��    '                     �                     5�_�   )   +           *          ����                                                                                                                                                                                                                                                                                                                                                             ep_     �         (    5��                          �                     5�_�   *   ,           +          ����                                                                                                                                                                                                                                                                                                                                                             ep`    �         *           �         )          5��                          �                     �                         �                     �                                              �                          �                     5�_�   +   -           ,           ����                                                                                                                                                                                                                                                                                                                                                             epb     �         *       �         *    5��                          �                     5�_�   ,   .           -          ����                                                                                                                                                                                                                                                                                                                                                             epc    �         +              return  �         *          def __str__(self):5��                                             �                                             �                         $                     5�_�   -   /           .          ����                                                                                                                                                                                                                                                                                                                                                             epi    �         +              return�         +    5��                                             5�_�   .   0           /   
   (    ����                                                                                                                                                                                                                                                                                                                                                             ep�    �   	      +      O    roles = models.ManyToManyField("Role", blank=True, related_name="managers")5��    	   (                  |                     5�_�   /   1           0   
   (    ����                                                                                                                                                                                                                                                                                                                                                             ep�   ! �   +            �   *   ,                  return self.name�   )   +              def __str__(self):�   (   *           �   '   )          0    allowed = models.BooleanField(default=False)�   &   (          (                            blank=False)�   %   '          '                            null=False,�   $   &          (                            unique=True,�   #   %          +    name = models.CharField(max_length=100,�   "   $          class Permission(models.Model):�   !   #           �       "           �      !                  return self.name�                     def __str__(self):�                 �                >                                         related_name="roles")�                4                                         blank=True,�                6    permissions = models.ManyToManyField("Permission",�                 �                (                            blank=False)�                '                            null=False,�                (                            unique=True,�                *    name = models.CharField(max_length=20,�                class Roles(models.Model):�                 �                 �                        return self.email�                    def __str__(self):�                 �                    REQUIRED_FIELDS = []�                    USERNAME_FIELD = "email"�                 �                !    objects = CustomUserManager()�   
              �   	             P    roles = models.ManyToManyField("Roles", blank=True, related_name="managers")�      
          *    email = models.EmailField(unique=True)�      	          $    # Models for all branch managers�                Iclass Managers(ManagersCommonFields, AbstractBaseUser, PermissionsMixin):�                 �                 �                'from .managers import CustomUserManager�                Ifrom django.contrib.auth.models import AbstractBaseUser, PermissionsMixin�                (from .common import ManagersCommonFields�                 from django.db import models5��                                                �               (       (          (       (       �               I       I   F       I       I       �               '       '   �       '       '       �                           �                       �                           �                       �               I       I   �       I       I       �               $       $         $       $       �               *       *   )      *       *       �    	           P       +   T      P       +       �    
                   .   �              .       �               !       ;   �      !       ;       �                           �                      �                      !   �             !       �                                               �                                               �                         ,                    �                          E                     �                          F                     �                          ]                     �                          w                     �               *           x      *               �               (          y      (              �               '       *   �      '       *       �               (       (   �      (       (       �                       '   �              '       �               6       (         6       (       �               4           9      4               �               >       6   :      >       6       �                       4   q              4       �                      >   �             >       �                          �                     �                           �                     �    !                      �                     �    "                                           �    #           +                 +               �    $           (                (              �    %           '       +   8      '       +       �    &           (       (   d      (       (       �    '           0       '   �      0       '       �    (                   (   �              (       �    )                  0   �             0       �    *                                           �    +                                    0       5�_�   0   2           1      $    ����                                                                                                                                                                                                                                                                                                                                                             e{�   " �      	   -      $    # Models for all branch managers5��                                            �                     	                	       �                                              5�_�   1   3           2          ����                                                                                                                                                                                                                                                                                                                                                             e{�   # �      	   -          # Models for TELLER,�      	   -    5��                      '                '       �       "                 &                    �       !                  %                     5�_�   2               3           ����                                                                                                                                                                                                                                                                                                                                                             e{�   % �      	   -      !    # Models for TELLER, MANAGER,�      	   -    5��               !       ,         !       ,       5��