Vim�UnDo� u�IST�$o���f���}��,�a��G�"BO      @    path("update-status/", update_status, name="update-status"),                             e$    _�                             ����                                                                                                                                                                                                                                                                                                                                                             e�7    �                �             5��                          �                      �                          �                      �                        �                     �                         �                      5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e�@     �               from customers.a�             5��                      >   �              >       5�_�                       I    ����                                                                                                                                                                                                                                                                                                                                                             e�F    �                    �   
            I    path("customer-details/", customer_details, name="customer-details"),5��    
   I                                      �                                              �                                               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             e�G    �                �             5��                       F                 F       5�_�                       E    ����                                                                                                                                                                                                                                                                                                                                                             e$�     �                   �             �             5��                          V                     �                      W   Z              W       5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e$�    �               [        path('customers/<int:profile_id>/', views.update_customer, name='update_customer'),5��                         Z                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e$�    �               W    path('customers/<int:profile_id>/', views.update_customer, name='update_customer'),5��       
       	          `      	              5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                             e$�     �               P    path('u /<int:profile_id>/', views.update_customer, name='update_customer'),�             5��                         V                    5�_�      
           	      4    ����                                                                                                                                                                                                                                                                                                                                                             e$�     �               ]    path('update-customer/<int:profile_id>/', views.update_customer, name='update_customer'),5��       .                  �                     5�_�   	              
      L    ����                                                                                                                                                                                                                                                                                                                                                             e$�    �               W    path('update-customer/<int:profile_id>/', update_customer, name='update_customer'),5��       K                 �                    5�_�   
                    E    ����                                                                                                                                                                                                                                                                                                                                                             e$�   	 �                F    path("update-customer/", update_customer, name="update-customer"),5��                                G               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e$,   
 �               W    path('update-customer/<int:profile_id>/', update_customer, name='update-customer'),5��                        *                    �                        +                    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e$4    �               W    path('update-customer/<sl :profile_id>/', update_customer, name='update-customer'),�             5��                                             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             e$�    �                �             5��                                               �                                               �                         !                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e$�    �               from accounts.a�             5��                      /                /       �                        )                    �                        *                    �       '                  9                     5�_�                       &    ����                                                                                                                                                                                                                                                                                                                                                             e$�     �               'from accounts.api_views.approve_account�             5��               '       <         '       <       5�_�                    
   F    ����                                                                                                                                                                                                                                                                                                                                                             e$�    �   
                 �   	            F    path("create-customer/", create_customer, name="create-customer"),5��    	   F                 �                     �    
                     �                     �    
                      �                     5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             e$�    �   
             �             5��    
                   @   �              @       5�_�                       ?    ����                                                                                                                                                                                                                                                                                                                                                             e$�    �               �                ]�                X    path('update-customer/<slug:profile_id>/', update_customer, name='update-customer'),�                I    path("customer-details/", customer_details, name="customer-details"),�                C    path("list-customers/", list_customers, name="list-customers"),�   
             @    path("update-status/", update_status, name="update-status"),�   	             F    path("create-customer/", create_customer, name="create-customer"),�      
          urlpatterns = [�      	          app_name = "customers"�                 �                <from accounts.api_views.approve_account import update_status�                >from customers.api_views.profile_update import update_customer�                Afrom customers.api_views.customer_details import customer_details�                8from customers.api_views.customers import list_customers�                :from customers.api_views.user_setup import create_customer�                 from django.urls import path5��                                                �               :       :          :       :       �               8       8   X       8       8       �               A       A   �       A       A       �               >       >   �       >       >       �               <       <         <       <       �                           O                      �                         P                    �                         g                    �    	           F       F   w      F       F       �    
           @       @   �      @       @       �               C       C   �      C       C       �               I       I   C      I       I       �               X       .   �      X       .       �                         �                    �                          �              $       5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e$f    �               <from accounts.api_views.approve_account import update_status5��                                            5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e$i    �               7from cu .api_views.approve_account import update_status�             5��                                             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e$�    �   
            @    path("update-status/", update_status, name="update-status"),5��    
                     �                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e$�    �   
            E    path("update-status/<sl >", update_status, name="update-status"),�             5��    
                  (   �             (       5�_�                       '    ����                                                                                                                                                                                                                                                                                                                                                             e$�    �               �                ]�                !         name='update-customer'),�                         update_customer,�                .    path('update-customer/<slug:profile_id>/',�                I    path("customer-details/", customer_details, name="customer-details"),�                C    path("list-customers/", list_customers, name="list-customers"),�   
             Q    path("update-status/<slug:profile_id>", update_status, name="update-status"),�   	             F    path("create-customer/", create_customer, name="create-customer"),�      
          urlpatterns = [�      	          app_name = "customers"�                 �                =from customers.api_views.approve_account import update_status�                >from customers.api_views.profile_update import update_customer�                Afrom customers.api_views.customer_details import customer_details�                8from customers.api_views.customers import list_customers�                :from customers.api_views.user_setup import create_customer�                 from django.urls import path5��                                                �               :       :          :       :       �               8       8   X       8       8       �               A       A   �       A       A       �               >       >   �       >       >       �               =       =         =       =       �                           P                      �                         Q                    �                         h                    �    	           F       F   x      F       F       �    
           Q       +   �      Q       +       �               C          �      C              �               I                I              �               .       C   #      .       C       �                      I   g             I       �               !       .   �      !       .       �                         �                    �                          �              $       5�_�                        )    ����                                                                                                                                                                                                                                                                                                                                                             e$    �   
            +    path("update-status/<slug:profile_id>",5��    
   )                  �                     5��