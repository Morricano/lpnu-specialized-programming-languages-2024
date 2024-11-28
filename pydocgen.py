import os
import pydoc

def generate_docs(root_dir, output_dir="docs"):
    """Генерує HTML-документацію для всіх .py файлів у проєкті."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Створює директорію для документації

    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".py"):
                module_path = os.path.splitext(os.path.relpath(os.path.join(root, file), root_dir))[0]
                module_name = module_path.replace(os.sep, ".")  # Перетворює шлях у формат модуля
                print(f"Генерація документації для модуля: {module_name}")
                try:
                    # Генерує HTML-документ для модуля
                    output_file = os.path.join(output_dir, f"{module_name.replace('.', '_')}.html")
                    with open(output_file, "w", encoding="utf-8") as f:
                        f.write(pydoc.html.document(pydoc.importfile(os.path.join(root, file))))
                except Exception as e:
                    print(f"Помилка для модуля {module_name}: {e}")

if __name__ == "__main__":
    generate_docs(".")  # Укажіть кореневу директорію вашого проєкту
