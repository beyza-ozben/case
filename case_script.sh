
cd /home/Masaüstü/proje/case

sudo find /home/ -printf '%s %p\n' | sort -nr | head -1

sudo find /home/ -printf '%s %p\n' | sort -nr | head -1 | awk '{ print $2 }'

FILE=$(sudo find /home/ -printf '%s %p\n' | sort -nr | head -1 | awk '{ print $2 }')

sha256sum "$FILE" > Big_Hash.txt

if [ ! -d /home/Masaüstü/proje/case.git ]; then
    git init
fi

# Değişiklikleri sahnele
git add .

# Commit mesajı
git commit -m "Cronjob çalıştı."

