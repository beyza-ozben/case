
cd Masaüstü/proje/case

FILE=$(sudo find /home/ -printf '%s %p\n' | sort -nr | head -1 | awk '{ print $2 }')

sha256sum "$FILE" | awk '{ print $1 }' > Big_Hash.txt

if [ ! -d /Masaüstü/proje/case.git ]; then
    git init
fi

# Değişiklikleri sahnele
git add .

# Commit mesajı
git commit -m "Cronjob çalıştı."

