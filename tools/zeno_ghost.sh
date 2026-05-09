#!/bin/bash
# Zeno-Ghost: Anti-Forensic Log Wiper

echo -e "\n============================================="
echo -e "   👻 ZENO-GHOST: FOOTPRINT ERASER"
echo -e "=============================================\n"

echo "[*] Wiping ~/.bash_history..."
cat /dev/null > ~/.bash_history && history -c

if [ -f ~/.zsh_history ]; then
    echo "[*] Wiping ~/.zsh_history..."
    cat /dev/null > ~/.zsh_history
fi

echo "[*] Unsetting HISTFILE variable..."
unset HISTFILE

echo "[+] Operations complete. Termux session is unlogged."
echo "[+] Self-destructing script..."
rm -- "$0"
