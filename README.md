# AT16-POST-WORDPRESS
#
Preconditions:
- Install XAMPP, WAMP, LAMP or MAMP
- Install Wordpress

Steps:
- Pull project https://github.com/AT16-APITESTING-G2/AT16-POST-WORDPRESS.git
- Move to "develop" branch
- Open project with Pycharm (recommend) or other code editor
- Install requirements.txt, for this use the command: pip install -r requirements.txt
- Create a folder for allure, for this use the command: py.test --alluredir=allure ./test
- Generate the report with the command: allure serve .\allure

-Create file .env with the next variables:
URI_TOKEN="http://localhost/wordpress/wp-json/api/v1/token"
USER_NAME="NAME_WORPRESS"
PASSWORD="PASSWORD_WORDPRESS"
URL="http://localhost/wordpress/wp-json/wp/v2/posts"