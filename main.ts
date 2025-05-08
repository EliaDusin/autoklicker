input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    if (Oliver == 0) {
        Oliver = 1
    } else {
        Oliver = 0
    }
})
input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    Häufigkeit += 100
})
input.onButtonEvent(Button.AB, input.buttonEventClick(), function () {
    Licht.set(LedSpriteProperty.X, randint(0, 4))
    Licht.set(LedSpriteProperty.Y, randint(0, 4))
})
input.onButtonEvent(Button.B, input.buttonEventClick(), function () {
    Häufigkeit += -100
})
let Oliver = 0
let Licht: game.LedSprite = null
let Häufigkeit = 1000
Licht = game.createSprite(2, 2)
Oliver = 0
basic.forever(function () {
    if (Oliver == 1) {
        Licht.set(LedSpriteProperty.X, randint(0, 4))
        Licht.set(LedSpriteProperty.Y, randint(0, 4))
        basic.pause(Häufigkeit)
    }
})
