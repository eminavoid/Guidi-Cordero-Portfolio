using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerBattle : MonoBehaviour
{
    [SerializeField] private float meleeDamage;
    [SerializeField] private float rangeDamage;
    [SerializeField] private int casillasAMover = 6;
    [SerializeField] private BattleManager battleManager;
    [SerializeField] private PlayersEventsManager playersEventsManager;
    [SerializeField] private float maxLife = 100;
    [SerializeField] private int stregth;
    [SerializeField] private int constitution;
    [SerializeField] private int wisdom;
    [SerializeField] private int armor;
    [SerializeField] private GameObject pointerPrefab;
    [SerializeField] private HealthBar barraDeVida;

    private float life;
    private Animator animator;
    private List<GameObject> playerList;
    private List<GameObject> enemyList;
    private int casillasMovidas = 0;
    private Vector3 StartPos;
    private Vector3 LastPos;
    private float NearObstacleDist;
    private Vector3 NearObstacleDistVect;
    private Vector3 NearObstaclePos = new Vector3(100, 100, 100);
    private int myTurn;
    private bool isMyTurn = false;
    private bool canRight = true;
    private bool canLeft = true;
    private bool canUp = true;
    private bool canDown = true;
    private bool canAttack = true;
    private bool isDead = false;



    public Vector3 Nearobstacledist { get; private set; }

    //public UnityEvent PassTurn = new UnityEvent();




    //Deteccion de entrar en colision con trigger que obtiene la posicion del objeto colisionado, la distancia tanto vectorial como en magnitud
    private void OnTriggerEnter2D(Collider2D collision)
    {
        NearObstaclePos = collision.gameObject.transform.position;
        NearObstacleDistVect = NearObstaclePos - gameObject.transform.position;
        NearObstacleDist = NearObstacleDistVect.magnitude;
        if (NearObstacleDistVect == Vector3.right)
        {
            canRight = false;
        }
        if (NearObstacleDistVect == Vector3.left)
        {
            canLeft = false;
        }
        if (NearObstacleDistVect == Vector3.up)
        {
            canUp = false;
        }
        if (NearObstacleDistVect == Vector3.down)
        {
            canDown = false;
        }

    }



    //Deteccion de salir de colision con trigger que obtiene la posicion del objeto colisionado, la distancia tanto vectorial como en magnitud
    private void OnTriggerExit2D(Collider2D collision)
    {
        NearObstaclePos = collision.gameObject.transform.position;
        NearObstacleDistVect = NearObstaclePos - gameObject.transform.position;
        NearObstacleDist = NearObstacleDistVect.magnitude;
        if (NearObstacleDistVect != Vector3.right)
        {
            canRight = true;
        }
        if (NearObstacleDistVect != Vector3.left)
        {
            canLeft = true;
        }
        if (NearObstacleDistVect != Vector3.up)
        {
            canUp = true;
        }
        if (NearObstacleDistVect != Vector3.down)
        {
            canDown = true;
        }

    }


    //Turno del player
    public void Turn()
    {
        enemyList = battleManager.EnemyListPost();
        //Se entra al turno basado en que trno determina el game manager
        if (isMyTurn && !isDead)
        {
            //Se entra si la cantidad de las casillas a mover es mayor que las que ya fueron movidas
            if (casillasAMover > casillasMovidas)
            {
                //Movimiento en base a botones teniendo en cuenta las colisiones
                if (Input.GetButtonUp("Up") && (canUp))
                {
                    LastPos = gameObject.transform.position;
                    transform.position = gameObject.transform.position + Vector3.up;
                    casillasMovidas++;
                }
                if (Input.GetButtonUp("Down") && (canDown))
                {
                    LastPos = gameObject.transform.position;
                    transform.position = gameObject.transform.position + Vector3.down;
                    casillasMovidas++;
                }
                if (Input.GetButtonUp("Right") && (canRight))
                {
                    LastPos = gameObject.transform.position;
                    transform.position = gameObject.transform.position + Vector3.right;
                    casillasMovidas++;
                }
                if (Input.GetButtonUp("Left") && (canLeft))
                {
                    LastPos = gameObject.transform.position;
                    transform.position = gameObject.transform.position + Vector3.left;
                    casillasMovidas++;
                }
            }

            //Boton de pasar turno
            if (Input.GetButtonDown("Pass Turn"))
            {
                battleManager.NextTurn();
                casillasMovidas = 0;
                canAttack = true;
                StartPos = gameObject.transform.position;
                isMyTurn = false;
            }

            if (Input.GetButtonUp("MeleeAttack") && canAttack)
            {
                animator.SetTrigger("isAttacking");
                enemyList = new List<GameObject>(battleManager.EnemyListPost());
                doDamage(enemyList[battleManager.WhichEnemyPost()], meleeDamage, 1);
            }

            if (Input.GetButtonUp("RangeAttack") && canAttack)
            {
                animator.SetTrigger("isMagic");
                enemyList = new List<GameObject>(battleManager.EnemyListPost());
                doDamage(enemyList[battleManager.WhichEnemyPost()], rangeDamage, 0);
            }

            //Boton de resetear posicion
            if (Input.GetButton("Reset"))
            {
                casillasMovidas = 0;
                transform.position = StartPos;
            }

        }
    }

    public void doMelee()
    {
        if (isMyTurn && !isDead && canAttack)
        {
            animator.SetTrigger("isAttacking");
            AudioManager.instance.PlaySFX("Sword");
            enemyList = new List<GameObject>(battleManager.EnemyListPost());
            doDamage(enemyList[battleManager.WhichEnemyPost()], meleeDamage, 1);
        }

    }

    public void doRange()
    {
        if (isMyTurn && !isDead && canAttack)
        {
            animator.SetTrigger("isMagic");
            AudioManager.instance.PlaySFX("Magic");
            enemyList = new List<GameObject>(battleManager.EnemyListPost());
            doDamage(enemyList[battleManager.WhichEnemyPost()], rangeDamage, 0);
        }
    }

    public void doPassTurn()
    {
        if (isMyTurn && !isDead)
        {
            battleManager.NextTurn();
            casillasMovidas = 0;
            canAttack = true;
            StartPos = gameObject.transform.position;
            isMyTurn = false;
        }
    }

    public float lifePost()
    {
        return life;
    }

    public float maxlifePost()
    {
        return maxLife;
    }

    public void changeTurn(bool turn)
    {
        isMyTurn = turn;
    }

    private void doDamage(GameObject enemigo, float damage, int typeOfDamage)
    {
        RaycastHit2D[] hit = Physics2D.LinecastAll(gameObject.transform.position, enemigo.gameObject.transform.position);
        RaycastHit2D[] hit2 = Physics2D.LinecastAll(enemigo.gameObject.transform.position, gameObject.transform.position);

        //Debug.Log(hit.Length);
        //Debug.Log(hit2.Length);

        if (hit[hit.Length - 1].collider.gameObject.TryGetComponent<Enemy>(out Enemy component))
        {
            //Debug.Log("hola");
            if (typeOfDamage == 0 && hit.Length >= 3)
            {
                //Debug.Log((((hit[hit.Length - 2].point - hit2[1].point).magnitude) / Mathf.Sqrt(2)));
                float actualDamage = (damage - (damage * (((hit[hit.Length - 2].point - hit2[1].point).magnitude) / Mathf.Sqrt(2))));
                //Debug.Log(damage * (((hit[hit.Length - 2].point - hit2[2].point).magnitude) / Mathf.Sqrt(2)));
                component.GetDamage(actualDamage);
                canAttack = false;
            }
            else if (typeOfDamage == 0 && hit.Length < 3)
            {
                component.GetDamage(rangeDamage);
                canAttack = false;
            }

            if (typeOfDamage == 1 && hit[hit.Length - 1].distance <= 1)
            {
                component.GetDamage(meleeDamage);
                canAttack = false;
            }

            if (component.lifePost() <= 0)
            {
                component.killEnemy();
                battleManager.popEnemyList(battleManager.WhichEnemyPost());
                battleManager.resetWhichEnemy();
            }
        }
    }
    //Funcion daño
    public void GetDamage(float attackDamage)
    {
        life -= attackDamage;
        barraDeVida.SetHealth();
        Debug.Log(life);
    }

    public void killPlayer()
    {
        isDead = true;
    }

    public void AssignTurn(int turn)
    {
        myTurn = turn;
    }

    private void Awake()
    {
        battleManager.PlayerPost(gameObject);
        enemyList = battleManager.EnemyListPost();
    }

    // Start is called before the first frame update
    void Start()
    {
        playersEventsManager.Melee.AddListener(doMelee);
        playersEventsManager.Range.AddListener(doRange);
        playersEventsManager.NextTurn.AddListener(doPassTurn);
        life = maxLife;
        animator = GetComponent<Animator>();
        StartPos = gameObject.transform.position;
        LastPos = gameObject.transform.position;
        NearObstacleDistVect = NearObstaclePos - gameObject.transform.position;
        NearObstacleDist = NearObstacleDistVect.magnitude;
    }


    // Update is called once per frame
    void Update()
    {
        if (!isDead)
        {
            Turn();
        }
        else if (isDead && isMyTurn)
        {
            //Debug.Log("HOLA");
            battleManager.NextTurn();
        }
        //Debug.Log(myTurn);
    }
}
