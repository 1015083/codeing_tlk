FUNCTION is_even(number)
    IF number MOD 2 EQUALS 0 THEN
        RETURN True
    ELSE
        RETURN False
    END IF
END FUNCTION

DISPLAY is_even(4)
DISPLAY is_even(7)
DISPLAY is_even(10)
DISPLAY is_even(3)
DISPLAY is_even(0)
 