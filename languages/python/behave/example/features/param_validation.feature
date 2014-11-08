Feature: Parameters validation

    Scenario: Query with no latitude
        Given service is running
        when I do not use latitude
        and I use a valid longitude
        and I do a poi request
        then service returns Bad Request
    
    Scenario: Query with no longitude
        Given service is running
        when I use a valid latitude
        and I do not use longitude
        and I do a poi request
        then service returns Bad Request
    
    Scenario: Query with invalid latitude
        Given service is running
        when I use an invalid latitude
        and I use a valid longitude
        and I do a poi request
        then service returns Bad Request
    
    Scenario: Query with minimum required parameters
        Given service is running
        when I use a valid latitude
        and I use a valid longitude
        and I do a poi request
        then service returns Bad Request 
