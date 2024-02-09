using System.Collections;
using System.Collections.Generic;
using System.Reflection;
using UnityEngine;
using UnityEngine.Events;
//using static UnityEditor.Progress;

public class BattleManager : MonoBehaviour
{

    private int turn = 1;
    [SerializeField] private Player player;
    [SerializeField] private Enemy enemy;
    [SerializeField] private GameObject pointerPrefab;
    [SerializeField] private GameObject gameManagerPrefab;

    private GameManager gameManager;
    private List<GameObject> playersList = new();
    private List<GameObject> enemyList = new();
    private List<GameObject> totalList = new();
    private Queue<GameObject> totalQueue = new();
    private List<int> turnList = new();
    private GameObject pointer;
    private int whichEnemy = 0;
    private bool EndBattle = false;

    public UnityEvent OnWin = new UnityEvent();
    public UnityEvent OnLose = new UnityEvent();

    public void NextTurn()
    {
        
        if (turn <= totalList.Count)
        {
            turn++;
        }
        if (turn > totalList.Count)
        {
            turn = 1;
        }
        var dequeuedObject = totalQueue.Dequeue();
        totalQueue.Enqueue(dequeuedObject);
        if (dequeuedObject.gameObject.TryGetComponent<Player>(out Player pobjectComponent))
        {
            pobjectComponent.changeTurn(true);
        }
        if (dequeuedObject.gameObject.TryGetComponent<Enemy>(out Enemy eobjectComponent))
        {
            eobjectComponent.changeTurn(true);
        }
    }

    //Saber que turno es
    public int QueTurno()
    {
        //Debug.Log(turn);
        return turn;
    }

    //Agregar a lista enemigos
    public void EnemyPost(GameObject gameObject)
    {
        //Debug.Log(gameObject.name);
        enemyList.Add(gameObject);
        totalList.Add(gameObject);
        totalQueue.Enqueue(gameObject);
    }

    //Agregar a lista players
    public void PlayerPost(GameObject gameObject)
    {
        //Debug.Log(gameObject.name);
        playersList.Add(gameObject);
        totalList.Add(gameObject);
        totalQueue.Enqueue(gameObject);
    }

    //Devolver que enemigo esta seleccionado
    public int WhichEnemyPost()
    {
        Debug.Log(whichEnemy);
        return whichEnemy;
    }

    // Start is called before the first frame update
    void Start()
    {
        EndBattle = false;
        pointer = Instantiate(pointerPrefab);
        gameManagerPrefab.TryGetComponent<GameManager>(out GameManager manager);
        gameManager = manager;
        for (int i = 1; i <= totalList.Count; i++)
        {
            turnList.Add(i);
        }

        foreach (var item in totalList)
        {
            //Debug.Log(turnList.Count);
            //Debug.Log(totalList.Count);
            int index = Random.Range(0, turnList.Count);

            if (item.gameObject.TryGetComponent<Enemy>(out Enemy enemyComponent))
            {
                enemyComponent.AssignTurn(turnList[index]);
                turnList.RemoveAt(index);
            }
            if (item.gameObject.TryGetComponent<Player>(out Player playerComponent))
            {
                playerComponent.AssignTurn(turnList[index]);
                turnList.RemoveAt(index);
            }
        }
        var dequeuedObject = totalQueue.Dequeue();
        totalQueue.Enqueue(dequeuedObject);
        if (dequeuedObject.gameObject.TryGetComponent<Player>(out Player pobjectComponent))
        {
            pobjectComponent.changeTurn(true);
        }
        if (dequeuedObject.gameObject.TryGetComponent<Enemy>(out Enemy eobjectComponent))
        {
            eobjectComponent.changeTurn(true);
        }
    }

    public void popEnemyList(int index)
    {
        //Debug.Log("entre en el pop con el indice" + index);
        enemyList.RemoveAt(index);
    }
    //Eliminar de la lista al player
    public void popPlayersList(int index)
    {
        playersList.RemoveAt(index);
    }
    //Resetear que enemigo esta seleccionado
    public void resetWhichEnemy()
    {
        whichEnemy = 0;
    }
    //Devolver lista de enemigos
    public List<GameObject> EnemyListPost()
    {
        return enemyList;
    }
    //Devolver lista de players
    public List<GameObject> PlayerListPost()
    {
        return playersList;
    }

    // Update is called once per frame
    void Update()
    {
        //Debug.Log(playersList.Count);
        if (enemyList.Count != 0)
        {
            pointer.gameObject.transform.position = enemyList[whichEnemy].gameObject.transform.position + Vector3.up;
            if (Input.GetButtonUp("Next"))
            {
                if (whichEnemy < enemyList.Count - 1)
                {
                    whichEnemy++;
                }
                else
                {
                    whichEnemy = 0;
                }

            }
            if (Input.GetButtonUp("Back"))
            {
                if (whichEnemy > 0)
                {
                    whichEnemy--;
                }
                else
                {
                    whichEnemy = enemyList.Count - 1;
                }

            }
        }

        if (enemyList.Count == 0 && !EndBattle)
        {
            turn = 0;
            EndBattle = true;
            AudioManager.instance.PlaySFX("Victory");
            Debug.Log("ganaste");
            OnWin.Invoke();
        }
        
        if (playersList.Count == 0 && !EndBattle)
        {
            turn = 0;
            EndBattle = true;
            AudioManager.instance.PlaySFX("Defeat");
            Debug.Log("perdiste");
            OnLose.Invoke();
        }
    }
}
