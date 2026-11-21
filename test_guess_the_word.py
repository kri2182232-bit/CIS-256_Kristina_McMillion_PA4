# Kristina McMillion
# CIS-256 Fall 2026
# Programming Assignment 4

import pytest

from guess_the_word import (
    WORD_LIST,
    choose_word,
    create_display_word,
    is_word_guessed,
    process_guess,
)

def test_choose_word_from_predefined_list():
    """Verify choose_word selects a word that belongs to the predefined list."""
    lowercase_word = [word.lower() for word in WORD_LIST]
    selected = choose_word(WORD_LIST)
    assert selected in lowercase_word

def test_choose_word_raises_on_empty_list():
    """Verify choose_word raises ValueError when given an empty list."""
    with pytest.raises(ValueError):
        choose_word([])

def test_correct_guess_reveals_single_and_repeated_letters():
    """Verify correct guesses are recorded without losing attempts and reveal 
    all matches."""
    guessed, attempts, status, _ = process_guess("christmas", set(), 6, "s")
    
    assert status == "correct"
    assert "s" in guessed
    assert attempts == 6
    assert create_display_word("christmas", guessed) == "_ _ _ _ s _ _ _ s"
 
def test_incorrect_guess_reduces_attempts():
    """Verify an incorrect guess reduces remaining attempt and records the letter."""
    gussed, attempts, status, _ = process_guess("grinch", set(), 6, "z")
 
    assert status == "incorrect"
    assert "z" in gussed
    assert attempts == 5
 
def test_duplicate_and_invalid_guessed_do_not_penalize():
    """Verify repeated or non-letter inputs do not reduce remaining attempts."""
    guessed_after_first, attempts_after_first, _, _ = process_guess(
        "whoville", set(), 6, "w"
    )
    guessed_dup, attempts_dup, dup_status, _ = process_guess(
        "whoville", guessed_after_first, attempts_after_first, "W"
    )
    guessed_inv, attempts_inv, inv_status, _ = process_guess(
        "whoville", guessed_dup, attempts_dup, "12"
    )
 
    assert dup_status == "duplicate"
    assert attempts_dup == 6
    assert inv_status == "invalid"
    assert attempts_inv == 6
    assert guessed_inv == {"w"}
 
def test_is_word_guessed_completion():
    """Verify word completion detection when all unique letters are guessed."""
    assert not is_word_guessed("grinch", {"g", "r", "i", "n", "c"})
    assert is_word_guessed("grinch", {"g", "r", "i", "n", "c", "h"})

