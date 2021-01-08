"""Esse módulo é utilizado para realizar testes automáticos dos exercícios."""

import unittest
from unittest.mock import patch
import main


class Test(unittest.TestCase):
    """Classe para agregar os métodos que serão utilizados para testar."""
    def test_ano_1984(self):
        """Função que testa 1984."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['1984']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 1
            mock_print.assert_called_with('O ano 1984 é bissexto.')

    def test_ano_2004(self):
        """Função que testa 2004."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['2004']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 1
            mock_print.assert_called_with('O ano 2004 é bissexto.')

    def test_ano_2024(self):
        """Função que testa 2004."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['2024']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 1
            mock_print.assert_called_with('O ano 2024 é bissexto.')

    def test_ano_1600(self):
        """Função que testa 1600."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['1600']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 1
            mock_print.assert_called_with('O ano 1600 é bissexto.')

    def test_ano_2000(self):
        """Função que testa 2000."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['2000']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 1
            mock_print.assert_called_with('O ano 2000 é bissexto.')

    def test_ano_2400(self):
        """Função que testa 2400."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['2400']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 1
            mock_print.assert_called_with('O ano 2400 é bissexto.')

    def test_ano_1800(self):
        """Função que testa 1800."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['1800']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 1
            mock_print.assert_called_with('O ano 1800 não é bissexto.')

    def test_ano_1900(self):
        """Função que testa 1900."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['1900']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 1
            mock_print.assert_called_with('O ano 1900 não é bissexto.')

    def test_ano_2100(self):
        """Função que testa 2100."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['2100']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 1
            mock_print.assert_called_with('O ano 2100 não é bissexto.')


if __name__ == '__main__':
    unittest.main()
