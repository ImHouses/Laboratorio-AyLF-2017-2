#!bin/bash
# Author: Juan Casas

case $1 in

	"date")
		# Busca todas las fechas con el formato DD/MM/AAAA
		echo "grep -E '(([0-2][1-9]|3[0-1]|20)\/(01|03|05|07|08|10|12)|([0-2][1-9]|30|20)\/(04|06|09|11)|([0-2][1-9]|20)\/02)\/[0-9]{4}'"
		grep -E '(([0-2][1-9]|3[0-1]|20)\/(01|03|05|07|08|10|12)|([0-2][1-9]|30|20)\/(04|06|09|11)|([0-2][1-9]|20)\/02)\/[0-9]{4}' $2 ;;
	"v1")
		# Busca todos los verbos en infinitivo; es decir, con terminación
		# ar, er, ir. Lidia con puntos y comas.
		echo "grep -E '((ar|er|ir),|(ar|er|ir)|(ar|er|ir).)$'"
		grep -E '((ar|er|ir),|(ar|er|ir)|(ar|er|ir).)$' $2 ;;
	"vr")
		# Reemplaza verbos en infinitivo por pretérito singular.
		echo "sed -E -e 's/(ar|er|ir)$/ó/g'"
		sed -E -e 's/(ar|er|ir)$/ó/g' $2 ;;
	"vcsv")
		# Verifica un CSV válido.
		echo "grep -E -i '([0-9a-z]+,|\"[0-9a-z]+\",)+'"
		grep -E -i '([0-9a-z]+,|"[0-9a-z]+",)+' $2 ;;
	"url")

		# Reemplaza en las URL que comienzan en http:// y terminan en .net
		# con https:// y .com respectivamente.
		echo "sed -E 's/(http|https):\/\/([0-9a-z]*(.*)).net?/https:\/\/\2.com/g'"
		sed -E 's/(http|https):\/\/([0-9a-z]*(.*)).net?/https:\/\/\2.com/g' $2 ;;
	"clean")
		#Limpiar
		sed -E 's/^(.*|".*"),/\L\1/;s/^(.*)((\n|\s),|,)$/\1.,/;s/(.*)\t/\1/;s/(.*)(\.\.)/1/' $2 ;;
	* )
		echo "USO: expresionesregulares.sh <COMANDO> <ARCHIVO>"
esac