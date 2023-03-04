Feature:PaintStores
  Background: PaintStores
    When Customer clicks on not now button

  Scenario:Successful Navigation to the Paint stores page
    Given Chrome is opened and asian paints app is opened
    When Customer is able to click on PaintStores link
    Then It shows PaintStores page

  Scenario: Successfully able to click view details button
    Given Chrome is opened and asian paints app is opened
    When Customer is able to click on PaintStores link
    And Customer is able to click on view details button
    Then It shows the page AP Beautiful homes furniture & Paint store for House Decoration

  Scenario: Successfully working of store locator button
    Given Chrome is opened and asian paints app is opened
    When Customer is able to click on PaintStores link
    And Customer enters pincode '122001'
    And Customer clicks on cookie close button
    And Customer is able to access store locator button
    Then  It shows the stores

  Scenario Outline: validate Enquire Now Functionality with valid data
      Given Chrome is opened and asian paints app is opened
      When Customer is able to click on PaintStores link
      When Customer enters <validname> and <validemail> and <validmobile> and <validpincode>
      And Customer clicks on cookie close button
      And Customer is able to click on Enquire Now Button
      Then it shows Thankyou image

    Examples:
      | validname   | validemail       | validmobile | validpincode   |
      | mehak       | mehak@gmail.com  | 6005888976  | 123456         |
      | sameet      | sameet@gmail.com | 7788654377  | 119988         |

  Scenario Outline: validate Enquire Now Functionality with invalid data
      Given Chrome is opened and asian paints app is opened
      When Customer is able to click on PaintStores link
      When Customer enters <invalidname> and <invalidemail> and <invalidmobile> and <invalidpincode>
      And Customer clicks on cookie close button
      And Customer is not able to click on Enquire Now Button
      Then It is on the same page

    Examples:
      | invalidname | invalidemail  | invalidmobile | invalidpincode |
      | @#$*        | mehakmail.com | 0123456789    | 123            |
      | ####        | samee43@      | 99@88$4       | 11998866       |
