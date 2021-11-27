def checking_HTML_correctness(filename):
  """
  Funkcja ma za zadanie sprawdzać poprawność składni dokumentu HTML.
  Jako argument przyjmuje nazwę pliku, który ma sprawdzić.
  Zwraca True jeśli dokument jest poprawny składniowo i False jeśli nie jest.
  """
  file_obj = open(filename, 'r')
  text = file_obj.read()