using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Events;

public class PlayersEventsManager : MonoBehaviour
{
    public UnityEvent Melee = new UnityEvent();
    public UnityEvent Range = new UnityEvent();
    public UnityEvent NextTurn = new UnityEvent();

    public void doMeleeAttack()
    {
        Melee.Invoke();
    }

    public void doRangeAttack()
    {
        Range.Invoke();
    }

    public void doNextTurn()
    {
        NextTurn.Invoke();
    }
}
