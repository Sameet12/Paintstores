Feature: PaintStores
    Background: PaintStores
    When Customer clicks on not now button

  Scenario: validate Enquire Now Functionality with valid data
      Given Chrome is opened and asian paints app is opened
      When  Customer is able to click on PaintStores link
      When  user enters <name> and <email> and <mobile> and <pincode>
      And Customer clicks on cookie close button
      And   Customer is able to click on Enquire Now Button
      Then  it shows valid search result page 2

