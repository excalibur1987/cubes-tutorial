from urllib import quote_plus

URI = "mssql+pyodbc:///?odbc_connect=" + quote_plus(CON_STRING_LOCAL)
