# Jak přispívat k Blender Addon Template

Děkujeme, že máte zájem vylepšit tuto šablonu! Jako veřejná šablona (template) uvítáme jakákoli vylepšení, která pomohou ostatním vývojářům psát čistší a stabilnější addony.

## 🛠️ Jak začít

1. **Forkněte** repozitář.
2. Vytvořte si **feature branch** (`git checkout -b feature/uzasna-funkce`).
3. Proveďte své změny.
4. Ujistěte se, že testy stále procházejí (`python3 -m unittest discover tests/unit`).
5. **Commitněte** změny s jasným popisem (podle konvencí Conventional Commits).
6. **Pushněte** do své větve a otevřete **Pull Request**.

## 📏 Pravidla pro kód

- Dodržujte **PEP 8**.
- Vždy oddělujte logiku (`core/`) od Blender API (`blender/`).
- Nové funkce by měly mít odpovídající testy v adresáři `tests/`.
- Dokumentujte kód pomocí docstringů (příprava pro automatickou dokumentaci).

## 🐛 Hlášení chyb

Pokud narazíte na chybu v šabloně, otevřete prosím **Issue** a popište:
- Co se stalo.
- Jak chybu reprodukovat.
- Verzi Blenderu, na které se problém projevil.

## 💡 Návrhy na vylepšení

Máte nápad, jak šablonu zjednodušit nebo vylepšit? Neváhejte otevřít Issue s označením `enhancement`.
