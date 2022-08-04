# AT16-POST-WORDPRESS
#

Preconditions:
- Install XAMPP, WAMP, LAMP or MAMP
- Install Wordpress
-Create file .env with the next variables:
URI_TOKEN="http://localhost/wordpress/wp-json/api/v1/token"
USER_NAME="NAME_WORPRESS"
PASSWORD="PASSWORD_WORDPRESS"
URL="http://localhost/wordpress/wp-json/wp/v2/posts"

For windows users:
- Open the Powershell terminal, and enter the next commands:
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser # Optional: Needed to run a remote script the first time
    irm get.scoop.sh | iex
    scoop install allure

Steps:
- Pull project https://github.com/AT16-APITESTING-G2/AT16-POST-WORDPRESS.git
- Move to "develop" branch
- Install requirements.txt, for this use the command: pip install -r requirements.txt
- Move to /test folder to run the test cases
- Create a folder for allure, for this use the command: py.test --alluredir=allure .
- Generate the report with the command: allure serve .\allure

