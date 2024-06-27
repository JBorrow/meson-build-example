module addition
    implicit none

contains
real function add_two(x)
        implicit none
        real, intent(in) :: x
        add_two = x + 2.0
end function add_two

end module
