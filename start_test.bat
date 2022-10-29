start "" "App\alttestdogcatrat.exe"

pytest -s pythontest\test_start_scene.py
pytest pythontest\test_start_button.py
pytest -s pythontest\test_main_menu.py
pytest pythontest\test_work_button.py
pytest pythontest\test_run_cat.py