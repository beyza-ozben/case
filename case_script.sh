#!/bin/bash

# Git deposunun bulunduğu dizine git
cd /home/Masaüstü/proje/case

 Değişiklikleri sahnele
git add .

# Commit mesajı
git commit -m "Otomatik commit"

# Değişiklikleri GitHub'a pushla
git push origin main

